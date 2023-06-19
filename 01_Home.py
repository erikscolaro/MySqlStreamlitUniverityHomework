import streamlit as st
from utils.utils import *

if __name__ == "__main__":
    st.set_page_config(
        page_title="Homepage",
        layout="wide",
        initial_sidebar_state="expanded"

    )

    st.title(":green[Web Application Development] with Streamlit and MySQL")

    col1, col2 = st.columns([3, 2], gap="small")

    with col1:
        st.header("Objective")
        st.markdown('Create a web application in Python (Streamlit) that interacts with a MySQL database to perform queries based on user interactions.')

    with col2:
        st.header("Dev: Erik Scolaro")
        st.markdown("- s301326@studenti.polito.it\n- Database Course, 2nd Year\n- Computer Engineering\n- Politecnico di Torino")

    st.header("Laboratory Specifications")
    st.markdown('1. Creation of a personalized Homepage using basic markdown syntax (or Streamlit elements) to introduce the laboratory, its objective, and the student.'
                '\n2. Creation of a page to display and filter available courses. The page should include two metrics to show the number of courses and distinct types available. The input widgets should be created to propose options based on the information already stored in the database. Users should be able to view course information by filtering through multiple categories (e.g., Type) and specifying the desired level range. In a separate expander, display the lesson programs for the selected courses. In case of empty results, an associated error/warning should be displayed.'
                '\n3. Creation of a page to display available instructors. Users should have the ability to filter by entering the instructor\'s last name and using a date range to select based on the birth date (hint: use datetime.date() to set the date_input and pass the date as a string in the query). The display should not be a comprehensive table, but divided element by element (create a dataframe and use df.iterrows to print one row at a time, see Lab 6). In case of empty results, a corresponding message should be displayed.'
                '\n4. Creation of a page to display charts regarding scheduled lessons. The page should include two charts: a Bar Chart showing the number of lessons per time slot and a Line Chart showing the number of scheduled lessons based on the day of the week.'
                '\n5. Creation of a page to add new courses through a suitable form. Use an insertion form that requires all the necessary data to add a new course to the database (CodC, Name, Type, Level). The application should verify that all fields are filled and that the value of the Level attribute is an integer between 1 and 4 (hint: use number_input). In case of missing data, duplicate keys, or other errors, the application should generate an error message. If the entered data is correct and the insertion operation is successful, a message confirming the successful insertion should be displayed.'
                '\n6. Creation of a form to insert a new weekly lesson into the PROGRAMMA table. The form should allow the user to enter all the necessary fields (CodFisc, Day, StartTime, Duration, CodC, Room) for programming a new lesson. The selection of the instructor should be done through a dropdown menu containing the fiscal codes of the possible instructors generated from the contents of the database table. Similarly, the course selection should be done through a dropdown menu populated from the database. The other fields should be manually populated by the user, using the most appropriate widgets (e.g., slider for StartTime and Duration) or text-based ones. The application should verify that the user does not try to schedule lessons that last more than 60 minutes and that the indicated day is a day between Monday and Friday. The insertion of a new lesson should be allowed and executed only if no other lessons for the same course are scheduled on the same day of the week (hint: use the input values to perform the query and check for records). If the insertion request complies with the indicated constraints and the insertion is successful, a message confirming the successful insertion should be displayed; otherwise, an error message should be shown (the error message should indicate the type of problem that caused the error).'
                '\n\nAll pages should be customized with text elements (using markdown or Streamlit pre-set widgets) to have titles, subtitles, and paragraphs that highlight what is being represented. In addition to generating the correct queries, to make the view and interface more intuitive and organized, the main layout elements should be used: expander, columns, tabs.')

    #connection to db
    check_connection()
