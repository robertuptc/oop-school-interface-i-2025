from classes.person import Person
import csv, os.path


class Student(Person):
    def __init__(self, name, age, password, role, school_id):
        super().__init__(name, age, password, role)
        self.school_id = school_id
    
    def __str__(self):
        print("\n")
        return f"{(self.name).upper()}\n------------------\nage: {self.age}\nid:{self.school_id}"


    @classmethod
    def all_students(cls):
        students = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")
        with open(path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                students.append(Student(**row))
        return students
