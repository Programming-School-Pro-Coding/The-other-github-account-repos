class Employee:
    def __init__(self, name, age, department, is_manager, is_department, rating, salary):
        self.name = name
        self.age = age
        self.department = department
        self.is_manager = is_manager
        self.is_department = is_department
        self.rating = rating # rating is from 1-5
        self.salary = salary

    def is_excellent(self):
        if self.rating >= 4.5:
            return True
        else:
            return False
    def bonus(self):
        if self.age == 60:
            self.salary += 50
            print("salary increased to " +str(self.salary))
        else:
            print("no bonus added, salary is still " +str(self.salary))