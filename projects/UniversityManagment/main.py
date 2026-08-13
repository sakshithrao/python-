import person


class Person:
    def __init__(self, id, name, age):
        self.name = name
        self.age = age
        self.id = id

class Student (Person):
    def __init__(self, id, name, age, student_id):
        super().__init__(id, name, age)
        self.student_id = student_id
class Employee (Person):
    def __init__(self, id, name, age, employee_id):
        super().__init__(id, name, age)
        self.employee_id = employee_id
        
class University (Student, Employee):
    def __init__(self, name):
        self.name = name
        self.students = {}
        self.employees = {}

    def add_student(self, student):
        self.students[student.id] = student

    def add_employee(self, employee):
        self.employees[employee.id] = employee
        
