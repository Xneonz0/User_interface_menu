class Student:
    def __init__(self, name, gender, student_id, age):
        self.name = name
        self.gender = gender
        self.student_id = student_id
        self.age = age

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_student_id(self):
        return self.student_id

    def get_age(self):
        return self.age

    def __str__(self):
        return f"Name: {self.name}, ID: {self.student_id}, Gender: {self.gender}, Age: {self.age}"
