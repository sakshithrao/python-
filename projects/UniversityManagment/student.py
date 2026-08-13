class Student(Person):
    def __init__(self, id, name, age, student_id):
        super().__init__(id, name, age)
        self.student_id = student_id