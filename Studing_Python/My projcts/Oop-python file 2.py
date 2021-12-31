#class Math:

#    @staticmethod
#    def add(x, y):
#        return x + y

#    @staticmethod
#    def add5(num):
#        return num + 5
#    
#    @staticmethod
#    def add10(num):
#        return num + 10

#    @staticmethod
#    def PI():
#        return 3.14
    
#    @staticmethod
#    def Mult(z , p):
#        return z * p

#    @staticmethod
#    def divide(w, t):
#        return w / t

#x = Math.add(5, 10)
#y = Math.add5(x)
#z = Math.add10(y)
#a = Math.Mult(2, 5)
#c = Math.divide(55, 2)
#print(x, c, y, z, a)
#print("-------------------------------------------")

#class Pizza:
#    def __init__(self, radius, ingredients):
#        self.radius = radius
#        self.ingredients = ingredients
    
#    def __str__(self):
#        return f"Pizza ingredients are {self.ingredients}"
#    
#    def area(self):
#        return Pizza.circle_area(self.radius)
    
#    @staticmethod
#    def circle_area(r):
#        return r ** 2 * Math.PI()

#p = Pizza(6, ['mozzarella', "Tomatoes"])
#print(p.area())
#print(Pizza.circle_area(4))
#print(Pizza.circle_area(10))

#class Dates:
#    def __init__(self, date):
#        self.__date = date
#    
#    def getDate(self):
#        return self.__date
#    
#    @staticmethod
#    def toDashDate(date):
#        return date.replace("/", "-")

#date = Dates("15-12-2016")
#dateFromDB = "15/12/2016"
#dateWithDash = Dates.toDashDate(dateFromDB)
#print(dateWithDash)

#if(date.getDate() == dateWithDash):
#    print("Equal")
#else:
#    print("Unequal")

#from datetime import date

#class Person:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
    
#    def display(self):
#        return f"name is {self.name} and age is {self.age}"
    
#    @classmethod
#    def initFromBirthYear(cls, name, birthYear, extra):
#        return cls(name, date.today().year - birthYear, extra)
    


#class Man(Person):
#    gender = "Male"
#    no_of_men = 0

#    def __init__(self, name, age, voice):
#        super().__init__(name, age)
#        self.voice = voice
#        Man.no_of_men += 1
        
#    def display(self):
#        string = super().display()
#        return string + f" and voice is {self.voice} and gender is {self.gender}"

#Man1 = Man("Mohamed", "12", "Hard")
#Man2 = Man("Anas", "8", "soft")
#Man3 = Man("Albaraa", "8", "soft")

#class Woman(Person):
#    gender = 'Female'
#    no_of_woman = 0

#    def __init__(self, name, age, hair):
#        super().__init__(name, age)
#        self.hair = hair
#        Woman.no_of_woman += 1
    
#    def display(self):
#        string = super().display()
#        return string + f" and hair is {self.hair} and gender is {self.gender}"

#woman1 = Woman("Amany", 32, "curly")

#man = Man.initFromBirthYear("Mohamed", 2009, "Hard")
#print(man.display())

#print("----------------------------------------")

#woman = Woman.initFromBirthYear("Amany", 1987, "curly")
#print(woman.display())

#print(isinstance(woman, Woman))
#print("------------------------------")
#print(isinstance(Man1, Man))

#from abc import ABC, abstractmethod
#class Shape(ABC):
#    @abstractmethod
#    def area(self):
#        pass

#    @abstractmethod
#    def perimeter(self):
#        pass

#class Square(Shape):
#    def __init__(self, side):
#        self.__side = side

#    def area(self):
#        return self.__side * self.__side 

#    def perimeter(self):
#        return self.__side * 4

#class Rect(Shape):
#    def __init__(self, length, width):
#        self.__length = length
#        self.__width = width
    
#    def area(self):
#        return self.__length * self.__width
    
#    def perimeter(self):
#        return (self.__length + self.__width) * 2

#square = Square(10)
#print(f"Square area is {square.area()} and perimeter is {square.perimeter()}")
#rect = Rect(5, 3)
#print(f"rectangle area is {rect.area()} and perimeter is {rect.perimeter()}")

