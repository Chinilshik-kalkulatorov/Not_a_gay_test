# Python Registration Program

This Python program allows a user to set up a username and password with certain requirements. It serves as a basic example of how a registration system might be implemented.



## Features
- Username input: Allows the user to set their desired username.
- Password input: Allows the user to set their password, ensuring  it's at least 12 characters long.
- Password verification: Asks the user to re-enter their password, verifying they know it, and provides opportunity for correction in case of mismatch.


## Algoritm

```mermaid
graph TB
    Start --> Init[Initialize AssessmentSystem]
    Init --> Register[Register User]
    Register --> CheckUser[Check if username exists]
    CheckUser --> UserExists[Username exists]
    CheckUser --> CreateUser[Create new user]
    CreateUser --> StudentCheck[Check if user is a student]
    StudentCheck --> AddStudent[Add to students]
    Init --> Login[Login User]
    Login --> CheckLoginUser[Check if username exists]
    CheckLoginUser --> UserNotFound[Username doesn't exist]
    CheckLoginUser --> VerifyPassword[Verify password]
    VerifyPassword --> IncorrectPassword[Password is incorrect]
    VerifyPassword --> SuccessfulLogin[Login successful]
    Init --> AddCourse[Add Course]
    AddCourse --> TeacherCheck1[Check if user is a teacher]
    TeacherCheck1 --> NotATeacher1[User is not a teacher]
    TeacherCheck1 --> CourseExistsCheck[Check if course exists]
    CourseExistsCheck --> CourseExists[Course exists]
    CourseExistsCheck --> CreateCourse[Create new course]
    Init --> AddScore[Add Score to Student]
    AddScore --> TeacherCheck2[Check if user is a teacher]
    TeacherCheck2 --> NotATeacher2[User is not a teacher]
    TeacherCheck2 --> StudentExistsCheck[Check if student exists]
    StudentExistsCheck --> StudentNotFound[Student doesn't exist]
    StudentExistsCheck --> CourseAndAssessmentCheck[Check course and assessment]
    CourseAndAssessmentCheck --> InvalidCourseOrAssessment[Invalid course or assessment]
    CourseAndAssessmentCheck --> AddStudentScore[Add score to student]
    Init --> ViewScores[View Student Scores]
    ViewScores --> StudentCheck2[Check if user is a student]
    StudentCheck2 --> NotAStudent[User is not a student]
    StudentCheck2 --> RetrieveScores[Retrieve student scores]
    Init --> GenerateReports[Generate Reports]
    GenerateReports --> CheckStudentExists[Check if student exists]
    CheckStudentExists --> StudentNotFound2[Student doesn't exist]
    CheckStudentExists --> CreateReports[Create overall and detailed reports]
    CreateReports --> End[End]

```


## Usage/Examples


Run the script in your Python environment. The program will guide you through the registration process.

```Python
while True:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if len(password) < 12:  # Check password length
        print("Password must be at least 12 characters. Please try again.")
        continue  # Return to start of loop

    password_check = input("Re-enter your password: ")

    if password == password_check:  # Check password match
        print("Registration successful.")
        break
    else:
        print("Passwords do not match. Please try again.")
```


## Run Locally

Run the script in your Python environment. The program will guide you through the registration process.

```bash
  python Testmile.py
```


## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

