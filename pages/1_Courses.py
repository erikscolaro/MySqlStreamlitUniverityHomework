import streamlit as st
from utils.utils import *
import pandas as pd

def create_metrics():
    col1, col2=st.columns(2)
    col1.metric(label="Number of courses", 
                value=execute_query(conn=st.session_state["connection"], 
                                    query="SELECT Count(*) FROM Corsi;").scalar())
    col2.metric(label="Avaiable couse types",
                value=execute_query(conn=st.session_state["connection"], 
                                    query="SELECT COUNT(*) FROM (SELECT DISTINCT Tipo FROM Corsi) AS Tabella;").scalar())

def create_filters():
    col1, col2=st.columns([3,2])
    query_courses_type=execute_query(conn=st.session_state["connection"],
                                     query="SELECT DISTINCT TIpo FROM Corsi;")
    
    selected_types=col1.multiselect(label="Filter by course type",
                                    options=[row[0] for row in query_courses_type])
    
    min_lv=execute_query(conn=st.session_state["connection"],
                                query="SELECT MIN(Livello) FROM Corsi").scalar()
    max_lv=execute_query(conn=st.session_state["connection"],
                                query="SELECT MAX(Livello) FROM Corsi").scalar()
    selected_levels=col2.slider(
        label="Filter by difficulty",
        min_value=min_lv,
        max_value=max_lv,
        value=(min_lv,max_lv)
    )

    return (selected_types, selected_levels)

def create_expander_programs(types, levels):
    if types==[]:
        st.warning(body="Select at least one course type to view related programs.")
    else:
        min_lv, max_lv=levels
        with st.expander(label="Programmi dei corsi selezionati", expanded=True):
            if len(types)==1:
                courses_query=execute_query(
                        conn=st.session_state["connection"],
                        query=f"SELECT CodC, Nome, Tipo, Livello FROM Corsi WHERE Tipo = '{types[0]}' AND Livello>={min_lv} AND Livello<={max_lv} ORDER BY Tipo, Nome, Livello;"
                    )
            else:
                courses_query=execute_query(
                        conn=st.session_state["connection"],
                        query=f"SELECT CodC, Nome, Tipo, Livello FROM Corsi WHERE Tipo IN {tuple(types)} AND Livello>={min_lv} AND Livello<={max_lv} ORDER BY Tipo, Nome, Livello;"
                    )
            
            courses_dict=[dict(zip(courses_query.keys(), result)) for result in courses_query]

            if courses_dict==list():
                st.error(body="No courses with the selected characteristics.")
            else:
                for course in courses_dict:
                    st.subheader(body=f"{course['Tipo']} - {course['Nome']} (lv {course['Livello']})")
                    program_query=execute_query(
                        conn=st.session_state["connection"],
                        query=f"SELECT CONCAT(Istruttore.Nome, ' ', Istruttore.Cognome) as Trainer, Programma.Giorno as Day, Programma.OraInizio as Starting_time, Programma.Durata as Duration, Programma.SalA as Room FROM Istruttore JOIN Programma ON Programma.CodFisc=Istruttore.CodFisc WHERE Programma.CodC='{course['CodC']}' ORDER BY Giorno, OraInizio"
                    )
                    df_program_query=pd.DataFrame(program_query)
                    
                    if df_program_query.empty:
                        st.error(body="No scheduled lessons for this course!")
                    else:
                        st.dataframe(data=df_program_query,use_container_width=True)

if __name__ == "__main__":
    st.title(":green[Course Search]")

    if st.session_state["connection"] is not False:
        create_metrics()
        (types, levels)=create_filters()
        create_expander_programs(types, levels)
    else:
        st.error('Connect to the database first!', icon="⚠️")

    #connection to db
    check_connection()
    