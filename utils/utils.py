import streamlit as st
from sqlalchemy import create_engine,text

"""Collect the principal functions shared by the various pages"""

def time_to_seconds(time_obj, duration):
    seconds = (time_obj.hour * 3600) + ((time_obj.minute+duration) * 60) + time_obj.second
    return seconds

def connect_db(dialect, username, password, host, dbname):
    try:
        engine=create_engine(f'{dialect}://{username}:{password}@{host}/{dbname}')
        conn=engine.connect()
        return conn
    except Exception as e:
        print(e)
        return False

def execute_query(conn, query):
    return conn.execute(text(query))

def check_connection():
    if "connection" not in st.session_state.keys():
        st.session_state["connection"] = False
    if st.sidebar.button("Connect to DB"):
        myconnection= connect_db(
            dialect="mysql+pymysql",
            username="user",
            password="password",
            host="localhost",
            dbname="palestra"
        )
        if myconnection is not False:
            st.session_state["connection"]=myconnection
            st.sidebar.success("Correctly connected to database.")
        else:
            st.session_state["connection"]=False
            st.sidebar.error("Error connecting to the database.")

def compact_format(num):
    num=float(num)
    if abs(num)>=1e9:
        return "{:.2f}B".format(num/1e9)
    elif abs(num)>=1e6:
        return "{:.2f}M".format(num/1e6)
    elif abs(num)>=1e3:
        return "{:.2f}K".format(num/1e3)
    else:
        return "{:.0f}".format(num)
