import streamlit as st
from utils.utils import *
import pandas as pd
import datetime

def create_bar_chart():
    passo=st.slider(label="Timeslot duration (minutes)", min_value=10, max_value=60, step=10)
    min_datetime=execute_query(conn=st.session_state["connection"],
                        query="SELECT STR_TO_DATE(MIN(OraInizio), '%H:%i:%s')  FROM Programma;").one()[0].total_seconds()/60
    max_datetime=execute_query(conn=st.session_state["connection"],
                        query="SELECT MAX(DATE_ADD(STR_TO_DATE(OraInizio, '%H:%i:%s'), INTERVAL Durata MINUTE)) FROM Programma;").one()[0].total_seconds()/60
    
    query=execute_query(conn=st.session_state["connection"],
                        query="SELECT STR_TO_DATE(OraInizio, '%H:%i:%s') as OraInizio, DATE_ADD(STR_TO_DATE(OraInizio, '%H:%i:%s'), INTERVAL Durata MINUTE) as OraFine FROM Programma ORDER BY OraInizio, Durata;")
    query_dict=[dict(Hours=datetime.time(hour=int(x/60), minute=x%60, second=0), Lessons_number=0) for x in range(int(min_datetime), int(max_datetime)+passo, passo)]
    
    for interval in query:
        for timeslot in query_dict:
            if interval[0]<=datetime.timedelta(hours=timeslot["Hours"].hour,minutes=timeslot["Hours"].minute+passo-1,seconds=59) and interval[1]>=datetime.timedelta(hours=timeslot["Hours"].hour,minutes=timeslot["Hours"].minute, seconds=1):
                timeslot['Lessons_number']+=1

    for timeslot in query_dict:
        timeslot['Hours']=timeslot['Hours'].strftime("%H:%M")
    df_query=pd.DataFrame(data=query_dict)
    st.bar_chart(data=df_query, use_container_width=True, x='Hours', y='Lessons_number')

def create_line_chart():
    query=execute_query(conn=st.session_state["connection"],
                        query="SELECT Giorno, Count(*) AS N FROM Programma GROUP BY Giorno")
    
    weekdays = [
    ("1.Monday", "1.Lunedì"),
    ("2.Tuesday", "2.Martedì"),
    ("3.Wednesday", "3.Mercoledì"),
    ("4.Thursday", "4.Giovedì"),
    ("5.Friday", "5.Venerdì"),
    ("6.Saturday", "6.Sabato"),
    ("7.Sunday", "7.Domenica")
]

    query_dict=[dict(weekday=G, weekday_ita=ITA, Lessons_number=0) for (G, ITA) in weekdays]
    for (G, N) in query:
        for d in query_dict:
            if d['weekday'][2:]==G: d['Lessons_number']=N
    st.line_chart(pd.DataFrame(data=query_dict),x='weekday', y='Lessons_number', use_container_width=True)

if __name__ == "__main__":
    st.title(":green[Scheduled lessons graph]")
    if check_connection() is not False:
        create_bar_chart()
        st.divider()
        create_line_chart()
    else:
        st.error('Connect to the database first!', icon="⚠️")