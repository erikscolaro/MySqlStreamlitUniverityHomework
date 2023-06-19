import streamlit as st
from utils.utils import *
import pandas as pd

def create_filters():
    col1, col2=st.columns(2)
    with col1:
        surname=st.text_input(label="Trainer surname", max_chars=20, placeholder="Rossi")
    with col2:
        min_datetime=execute_query(conn=st.session_state["connection"],
                                   query="SELECT MIN(DataNascita) FROM Istruttore;").one()[0]
        max_datetime=execute_query(conn=st.session_state["connection"],
                                   query="SELECT MAX(DataNascita) FROM Istruttore;").one()[0]
        (min_born_date, max_born_date)=st.date_input(label="Birth date range", min_value=min_datetime, max_value=max_datetime, value=(min_datetime, max_datetime))
    return (surname, (min_born_date, max_born_date))

def create_trainer_info(surname, min_datetime, max_datetime):
    found_trainers=execute_query(conn=st.session_state["connection"],
                        query=f"SELECT CONCAT(Cognome, ' ', Nome) as Trainer, CodFisc as ID_Code, DataNascita as Birth_date, Email, Telefono as Mobile FROM Istruttore WHERE Cognome LIKE '{surname}%' AND DataNascita BETWEEN '{min_datetime}' AND '{max_datetime}';")
    df_found_trainers=pd.DataFrame(found_trainers)
    if df_found_trainers.empty:
        st.error(body="No trainers found.")
    else:
        with st.container():
            for index, row in df_found_trainers.iterrows():
                st.markdown(body=f"{index+1}.  **:green[{row['Trainer']}]** - CF: {row['ID_Code']} - Email: - {row['Email']} - Tel: {row['Mobile']}")

if __name__ == "__main__":
    st.title(":green[Trainer search]")

    if st.session_state["connection"] is not False:
        (surname, (min_datetime, max_datetime))=create_filters()
        create_trainer_info(surname, min_datetime, max_datetime)
    else:
        st.error('Connect to the database first!', icon="⚠️")
    