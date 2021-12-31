class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display(self):
        return f"your name is {self.name} and your age is {self.age} and your grade {self.grade}"


student1 = Student("Mohamed", "12", "fifth")
student2 = Student("Anas", "8", "second")
student3 = Student("Albaraa", "8", "second")
student4 = Student("Islam", "13", "fifth")
print(student1.display())
print(student2.display())
print(student3.display())
print(student4.display())