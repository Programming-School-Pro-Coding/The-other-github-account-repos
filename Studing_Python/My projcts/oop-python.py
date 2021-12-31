#x = "codezilla"
#print(x.upper())
#print(type(x))
#print(2 * 3)
#print("Mohamed " + " is " + " cool")
from datetime import date

class Student:
    def __init__(self, name, age=0):
        self.__name = name
        self.__age = age
    
#    def get_name(self):
#        return self.__name
    
#    def set_name(self, new_name):
#        self.__name = new_name
    
#    def get_age(self):
#        return self.__age
    
#    def set_age(self, new_age):
#        self.__age = new_age
    
    def describe(self):
        print(f"My name is {self.__name} and my age is {self.__age}")
    
#    def is_old(self, num):
#        if self.__age < num:
#            print("student is not old")
#        elif self.__age > num:
#            print("Student is old")
#        elif self.age == num:
#            print("Student is equal")
#        else:
#            print("student is young")
   
    @classmethod
    def initFromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)
        

#student_1 = Student("Mohamed", 12, ["programing", "python","Javascript"])
#student_2 = Student("Anas", 9)
#student_3 = Student("Albaraa", 9)
#student_2.name = "Ahmed"
#student_2.age = 60
#print(student_3.age, student_2.name, student_2.age, student_1)
#print(Student.no_of_students)
#student_1.describe()
#student_4.is_old(30)
#student_4.name = "Mohamed"
#print(student_4.get_name())
#student_4.grade = "fifth"
#print(student_4.grade)
#print(student_4.name)
#student_4.describe()
#student_4.set_name("Mohamed")
#student_4.set_age(50)
#student_1 = Student("Islam", 12)
#student_2 = Student.initFromBirthYear("Mohamed", 2009)
#student_1.describe()
#student_2.describe()


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    
    @classmethod
    def veg(cls):
        return cls(["mushrooms", 'olives', "onions", "Tomato"])

    @classmethod
    def marherita(cls):
        return cls (['mozarella', "saude", 'onions', "Tomato"])

    def __str__(self):
        return f"Pizza ingredients are {self.ingredients}"

pizza1 = Pizza(['tomatoes', "olives"])
pizza2 = Pizza.veg()
pizza3 = Pizza.marherita()

print(pizza1)
print(pizza2)
print(pizza3)

