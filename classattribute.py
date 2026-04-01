class Student:
    # Class attribute
    college_name = "ABC University"
    
    def __init__(self, name, age, roll_number):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute
        self.roll_number = roll_number  # Instance attribute

    def attend_class(self):
        print(f"{self.name} from {Student.college_name} is attending the class.")
        # Accessing class attribute using class name

# Creating Student objects
student_1 = Student('Amit', 20, 'S123')
student_2 = Student('Priya', 19, 'S124')

student_1.attend_class()
student_2.attend_class()

# Accessing class attribute directly through class name
print(Student.college_name)

# Accessing class attribute through an object reference
print(student_1.college_name)