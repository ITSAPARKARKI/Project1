# Project1
# Student Management System

A beginner-friendly Student Management System built using Python and MySQL. This project allows users to manage student records through a simple command-line interface.

## Features

- Add new students
- Display all student records
- Search students by ID
- Update student information
- Delete student records
- View student statistics (total, average, highest, and lowest grades)

## Technologies Used

- Python
- MySQL
- MySQL Connector
- python-dotenv
- Git and GitHub

## Project Structure

```text
Project1/
├── .vscode/
├── src/
│   ├── main.py
│   ├── student.py
│   ├── connection.py
│   └── .env
├── .gitignore
└── README.md
```

## Setup Instructions

1. Clone this repository.
2. Install the required packages:

```bash
pip install mysql-connector-python python-dotenv
```

3. Create a MySQL database named `student_management`.
4. Create the `STUDENT` table.
5. Create a `.env` file inside the `src` folder with your database credentials.
6. Run the application:

```bash
python3 src/main.py
```


## Author

Apar
