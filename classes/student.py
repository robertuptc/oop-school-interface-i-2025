from classes.person import Person
import csv


class Student(Person):
    def __init__(self, name, age, password, role, school_id):
        super().__init__(name, age, password, role)
        self.school_id = school_id
    
    def all_students():
        students = []
        with open('data/students.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                students.append(row)
        return students
