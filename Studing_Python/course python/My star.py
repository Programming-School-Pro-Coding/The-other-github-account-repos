import turtle


k = turtle.Turtle()

def star():
    for i in range(5):
        k.forward(50)
        k.right(144)
        k.end_fill()

def goto():
    for x in range(1):
        k.penup()
        k.goto(-50, 50)
        k.pendown()

def square():
    for l in range(4):
        k.forward(150)
        k.left(90)

while True:
    star()
    goto()
    square()
    break