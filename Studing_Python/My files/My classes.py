class Math:
    def add(b, a):
        return b + a

    def subs(f, k):
        return f - k

    def mult(s, o):
        return s * o

    def divid(v, g):
        return v / g

    def Module(w, l):
        return w % l


class MyFamily:
    def __init__(self, name, age):
        self.name = name

    def display():
        return f"Your name is {self.name} and your age is {self.age}"


class Students:
    def __init__(self, name, grade, age="Mohamed"):
        self.name = name
        self.age = age
        self.grade = grade

    def display():
        return f"Your name is {self.name} and  your age is {self.age} and your grade is {self.grade}"


class Course:
    def __init__(self, name, age, kind_of_course):
        self.name = name
        self.age = age
        self.kind_of_course = kind_of_course

    def display():
        print(
            f"Your name is {self.name} and your age is {self.age} and your kind of course {self.kind_of_course}")


student1 = Students("Mohamed", "fifth", "12")
print(student1.display())
