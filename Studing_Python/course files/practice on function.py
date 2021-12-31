import turtle

t = turtle.Turtle()
a = turtle.Turtle()
f = turtle.Turtle()
r = turtle.Turtle()


# increase number by ...
def increase(num, by):
    return num + by


# Draw a square
def Draw_square(side, robot):
    for i in range(4):
        t.forward(side)
        t.left(90)


# Draw rectangle
def Draw_rectangle(a, b):
    for i in [a, b, a, b]:
        t.forward(i)
        t.left(90)


# Draw_square(100, t)
# Draw_square(150, a)
# Draw_square(200, f)
# Draw_square(250, r)
Draw_rectangle(100, 50)
