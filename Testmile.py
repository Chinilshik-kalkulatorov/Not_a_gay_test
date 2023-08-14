# Sample Python Code for Student Assessment Management System

class AssessmentSystem:
    def __init__(self):
        # Initializing user and grades databases
        self.users = {'admin': 'password123'}
        self.grades = {}

    def login(self, username, password):
        # Check if the username and password match the database
        if username in self.users and self.users[username] == password:
            return "Access granted"
        else:
            return "Access denied"

    def view_grades(self, studentID):
        # Retrieve grades for a specific student
        return self.grades.get(studentID, "No grades available")

    def add_edit_grades(self, studentID, assessment, grade):
        # Add or edit grades for a student
        if studentID not in self.grades:
            self.grades[studentID] = {}
        self.grades[studentID][assessment] = grade
        return "Grade updated"

    def feedback(self, studentID, message):
        # Send feedback to a student's teacher (placeholder function)
        return "Feedback sent to teacher"
