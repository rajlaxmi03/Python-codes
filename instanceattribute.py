class Student:
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll Number: {self.roll_number}")

# Creating Student objects
student_1 = Student('Rahul', 21, 'S125')
student_2 = Student('Neha', 22, 'S126')

student_1.display_info()
student_2.display_info()