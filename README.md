# Assessment Management System

## Overview
The Assessment Management System is designed to manage and track student assessment results for an international college. The system provides functionalities for user registration, login, course addition, score management, and report generation.

## Features

### User Registration
- Allows both students and teachers to register with a unique username and password.
- Automatically categorizes users as either a student or a teacher based on registration details.

### User Login
- Users can log in using their registered username and password.
- Ensures data security by verifying user credentials before granting access.

### Course Management
- Teachers can add new courses along with their respective assessments.
- Each course can have multiple assessments.

### Score Management
- Teachers can add scores for students based on their assessments.
- Scores can be added for individual assessments as well as combined totals for their courses.

### Report Generation
- Provides two types of reports:
  1. Overall Performance Report: Shows the average score of a student across all assessments in a course.
  2. Detailed Course Report: Provides a breakdown of scores for each assessment in a course.

## Algorithm

The flow of operations within the `AssessmentSystem` class is visualized using the following Mermaid diagram:

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


```


## Run Locally

Run the script in your Python environment. The program will guide you through the registration process.

```bash
  python Testmile.py
```


## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

