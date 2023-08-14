class AssessmentSystem:
    def __init__(self):
        self.users = {}  
        self.courses = {} 
        self.students = {}
        self.logged_in_user = None

    def register(self, username, password, status):
        if username in self.users:
            return "Username already exists!"
        user_id = len(self.users) + 1
        self.users[username] = {"password": password, "status": status, "id": str(user_id)}
        if status == "student":
            self.students[str(user_id)] = {"first_name": username.split()[0], "last_name": username.split()[1], "courses": {}}
        return f"{status.capitalize()} {username} registered successfully!"
    
    def login(self, username, password):
        if username not in self.users:
            return "Username doesn't exist!"
        if self.users[username]["password"] != password:
            return "Wrong password!"
        self.logged_in_user = username
        return f"Welcome {username}!"
    
    def add_course(self, course_name, assessments):
        if not self.logged_in_user or self.users[self.logged_in_user]["status"] != "teacher":
            return "Only teachers can add courses!"
        if course_name in self.courses:
            return "Course already exists!"
        self.courses[course_name] = assessments
        return f"Course {course_name} added successfully!"
    
    def add_score(self, student_id, course_name, assessment_name, score):
        if not self.logged_in_user or self.users[self.logged_in_user]["status"] != "teacher":
            return "Only teachers can add scores!"
        if student_id not in self.students:
            return "Student doesn't exist!"
        if course_name not in self.courses or assessment_name not in self.courses[course_name]:
            return "Invalid course or assessment!"
        if course_name not in self.students[student_id]["courses"]:
            self.students[student_id]["courses"][course_name] = {}
        self.students[student_id]["courses"][course_name][assessment_name] = score
        return f"Score added successfully for Student {student_id}!"
    
    def view_scores(self, student_id):
        if not self.logged_in_user or self.users[self.logged_in_user]["status"] != "student":
            return "Only students can view scores!"
        if student_id not in self.students:
            return "Student doesn't exist!"
        return self.students[student_id]["courses"]

    # Generate reports for Robert
    def generate_reports(self, student_id):
        if student_id not in self.students:
            return "Student doesn't exist!"
        
        # 1. Overall performance report
        overall_performance = {}
        for course, assessments in self.students[student_id]["courses"].items():
            overall_performance[course] = sum(assessments.values()) / len(assessments)
        
        # 2. Detailed course report
        detailed_report = self.students[student_id]["courses"]
        
        return {"Overall Performance": overall_performance, "Detailed Report": detailed_report}

# Testing the reports function
system = AssessmentSystem()
system.register("Mr Smith", "teacher_pass", "teacher")
system.register("John Doe", "student_pass", "student")
system.login("Mr Smith", "teacher_pass")
system.add_course("Math", ["Assessment1", "Assessment2"])
system.add_score("2", "Math", "Assessment1", 85)
system.add_score("2", "Math", "Assessment2", 90)
reports = system.generate_reports("2")
reports
