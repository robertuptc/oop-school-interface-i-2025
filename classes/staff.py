from classes.person import Person
import csv

class Staff(Person):
    def __init__(self, name, age, password, role, employee_id):
        super().__init__(name, age, password, role)
        self.employee = employee_id

    def all_staff():
            staff = []
            with open('data/staff.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    staff.append(row)
            return staff
