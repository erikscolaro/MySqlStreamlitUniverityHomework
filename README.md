# Gym Management System with Streamlit and MySQL

A web application built with Python (Streamlit) that interacts with a MySQL database to manage gym courses, instructors, and lesson schedules. This project was developed as part of a Database Course at Politecnico di Torino.

## Description

This application allows users to:
- View and filter available courses by type and difficulty level
- Search for instructors by surname and birth date
- Visualize scheduled lessons through charts
- Add new courses and schedule new lessons
- Connect to a MySQL database to perform queries based on user interactions

## Prerequisites

- Python 3.9+
- MySQL Server
- The following Python libraries:
    - pandas==2.0.1
    - SQLAlchemy==2.0.12
    - streamlit==1.22.0
    - PyMySQL==1.0.3
    - cryptography==40.0.2
    - urllib3==1.26.6
    - watchdog

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/gym-management-system.git
cd gym-management-system
```

2. Set up a virtual environment (optional but recommended)
```bash
# Using pipenv
pipenv install

# Or using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up a MySQL database named "palestra" with the required tables:
     - Corsi (courses)
     - Istruttore (instructors)
     - Programma (schedule)

## Usage

1. Start the Streamlit application
```bash
streamlit run 01_Home.py
```

2. Connect to the database by clicking the "Connect to DB" button in the sidebar. The default configuration is:
     - Username: user
     - Password: password
     - Host: localhost
     - Database: palestra

3. Navigate through the different pages using the sidebar:
     - Home: Overview and project information
     - Courses: View and filter available courses
     - Trainers: Search for instructors
     - Scheduled lessons: View charts of lesson schedules
     - Add new course: Form to add new courses
     - Add new lesson: Form to schedule new lessons

## Project Structure

- `01_Home.py`: Main entry point for the Streamlit application
- `pages/`: Directory containing additional application pages
    - `1_Courses.py`: Page to view and filter courses
    - `2_Trainers.py`: Page to search for instructors
    - `3_Scheduled_lessons.py`: Charts for scheduled lessons
    - `4_Add_new_course.py`: Form to add new courses
    - `5_Add_new_lesson.py`: Form to schedule new lessons
- `utils/`
    - `utils.py`: Shared functions used across pages
- `requirements.txt`: List of Python dependencies
- `.streamlit/config.toml`: Streamlit configuration (theme, etc.)

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a new Pull Request