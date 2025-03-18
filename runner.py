from classes.school import School
from classes.student import Student
from classes.staff import Staff
from classes.school import School

school = School('Ridgemont High')


while True :
    mode = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")
    if mode == '1':
        school.list_students()
    elif mode == '2':
        student_id = input("Enter student ID: ")
        student = school.find_student_by_id(student_id)
    elif mode == '3':
        pass
    elif mode == '4':
        pass
    else:
        break



# print(school.name)

# student_info = {'name' : 'Diana', 'password' : 'password', 'school_id' : 12345, 'age' : 17, 'role' : 'Student'}
# student_one = Student(**student_info)
# print(student_one.name)

# all_students = Student.all_students()
# print(all_students)

# all_staff = Staff.all_staff()
# print(all_staff)