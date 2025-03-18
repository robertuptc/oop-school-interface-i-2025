from classes.student import Student
from classes.staff import Staff

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_staff()
        self.students = Student.all_students()
    
    def list_students(self):
        print("\n")
        for idx, student in enumerate(self.students):
            print(f"{idx + 1}. {student.name} {student.school_id}")
            # print(student['name'])
    
    def find_student_by_id(self, id):
        for student in self.students:
            if student.school_id == id:
                print(student)
