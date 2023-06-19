import streamlit as st
from utils.utils import *
from datetime import time

def create_form():
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    avaiable_codc=list()
    for row in execute_query(conn=st.session_state["connection"],
                             query="SELECT CodC FROM Corsi;"):
        avaiable_codc.append(row[0])
    avaiable_codf=list()
    for row in execute_query(conn=st.session_state["connection"],
                                   query="SELECT CodFisc FROM Istruttore;"):
        avaiable_codf.append(row[0])


    with st.form("New scheduled lesson"):
        codf=st.selectbox(label="Trainer ID code selection", options=avaiable_codf)
        cols = st.columns(5)
        with cols[0]:
            codc=st.selectbox(label="Course selection", options=avaiable_codc)
        with cols[1]:
            giorno=st.selectbox(label="Course day selection ", options=weekdays)
        with cols[2]:
            orainizio=st.time_input(label="Start time selection", step=300, value=time(hour=8))
        with cols[3]:
            durata=st.number_input(label="Course duration", max_value=60, step=5, min_value=5, value=30)
        with cols[4]:
            sala=st.text_input(label="Room number", max_chars=5, placeholder="S****")
        
        submitted= st.form_submit_button("Submit", type='primary')

        if submitted: 
            if sala=='': 
                st.warning(body="Insert the room number first.")
            else:
                overlaps=execute_query(conn=st.session_state["connection"], 
                                    query=f"SELECT STR_TO_DATE(OraInizio, '%H:%i:%s') as OraInizio, DATE_ADD(STR_TO_DATE(OraInizio, '%H:%i:%s'), INTERVAL Durata MINUTE) as OraFine FROM Programma WHERE CodC='{codc}' AND Giorno='{giorno}' ORDER BY OraInizio, Durata;")
                flag=True
                for row in overlaps:
                    if not (time_to_seconds(orainizio, durata)<=row[0].total_seconds() or time_to_seconds(orainizio,0)>=row[1].total_seconds()):
                        flag=False

                if flag==False:
                    st.error(body="There's at least another scheduled lesson for the same course that overlap with the selected time.")
                else:
                    execute_query(conn=st.session_state["connection"],
                                    query=f"INSERT INTO Programma (CodFisc, Giorno, OraInizio, Durata, Sala, CodC) VALUES ('{codf}','{giorno}','{orainizio}',{durata},'{sala}','{codc}');")
                    st.success(body="Insertion to database successful.")

if __name__ == "__main__":
    st.title(":green[Add new scheduled lesson for a specific course]")
    if check_connection() is not False:
        create_form()