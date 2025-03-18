from classes.school import School
from classes.student import Student
from classes.staff import Staff

school = School('Ridgemont High')
# print(school.name)

student_info = {'name' : 'Diana', 'password' : 'password', 'school_id' : 12345, 'age' : 17, 'role' : 'Student'}
student_one = Student(**student_info)
# print(student_one.name)

all_students = Student.all_students()
print(all_students)

all_staff = Staff.all_staff()
print(all_staff)