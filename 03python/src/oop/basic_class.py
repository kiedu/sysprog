class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Roll Number: {self.roll_number}"

student1 = Student("John Doe", 18, 1234)
print(student1.get_details())	