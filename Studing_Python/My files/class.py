class My_Family:
    num_of_Family = 0
    def __init__(self, name, age, grade="finished school"):
        self.name = name
        self.age = age
        self.grade = grade
        My_Family.num_of_Family += 1
    
    def display(self):
        return f"The name is {self.name} and the age is {self.age} and the grade is {self.grade}"

person1 = My_Family("Mohamed", 12, "grade 5")

print(person1.display())
print(isinstance(person1, My_Family))
print(My_Family(num_of_Family))