import streamlit as st
from utils.utils import *

def create_form():
    reserved_codc=list()
    for row in execute_query(conn=st.session_state["connection"],
                                   query="SELECT CodC FROM Corsi;"):
        reserved_codc.append(row[0])
    with st.form("New course entry form"):
        codc=st.text_input("Course code", placeholder="CT***", max_chars=10)
        nome=st.text_input("Course name", max_chars=50, placeholder="Spinning")
        tipo=st.text_input("Course type", max_chars=50, placeholder="Cardio")
        livello=st.number_input(label="Course difficulty level", min_value=1, max_value=4)

        submitted= st.form_submit_button("Submit", type='primary')

        if submitted: 
            if codc=='' or nome=='' or tipo=='': st.warning(body="Be sure to fill all the form fields.")
            elif codc in reserved_codc: st.error(body="Course code alredy used, try entering another one.")
            else:
                execute_query(conn=st.session_state["connection"],
                                   query=f"INSERT INTO Corsi (CodC, Nome, Tipo, Livello) VALUES ('{codc}','{nome}','{tipo}',{livello})")
                st.success(body="Inserction to database successfull")



if __name__ == "__main__":
    st.title(":green[Add new course]")
    if check_connection() is not False:
        create_form()