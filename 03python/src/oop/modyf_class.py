class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        
    def get_Person_info(self):
        return f"Name: {self.firstName} {self.lastName}, Age: {self.age}"

class Student(Person):
    def __init__(self, firstName, lastName, age, phoneNumber, creditCard):
        #Person.__init__(self, firstName, lastName, age)
        super().__init__(firstName, lastName, age)
        self._phoneNumber = phoneNumber
        self.__creditCard = creditCard

    def get_Student_info(self):
        return f"Name: {self.firstName} {self.lastName}, Age: {self.age}, {self._phoneNumber}, {self.__creditCard} "

student1 = Student("John", "Doe", 18, "+380671234567", "4561 1236 7894 1230")
print(student1.get_Student_info())
print(student1._phoneNumber) # protected variable can be accessed
print(student1.__creditCard) # private variable cannot be accessed