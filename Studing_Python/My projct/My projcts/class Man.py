class Man():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __add__(self, other):
        names = self.name + " and " + other.name
        ages = self.age + other.age
        return f"names combined are {names} and sum of ages is {ages}"

    def __lt__(self, other):
       return self.age < other.age
        
    def display(self):
        return f"name is {self.name} and age is {self.age}"

#Man1 = Man("Mohamed", "12", "Hard")
#Man2 = Man("Anas", "8", "soft")
#Man3 = Man("Albaraa", "8", "soft")
man = Man("Islam", 20)
man2 = Man("Ahmed", 30)
#print(man+man2)
print(man<man2)
print(dir(Man))