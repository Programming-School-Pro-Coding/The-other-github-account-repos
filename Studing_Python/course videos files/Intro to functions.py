import turtle

t = turtle.Turtle()

#functions
#user-defind
def square():
    for i in range(4):
        t.forward(100)
        t.left(90)

square()
t.forward(200)
square()