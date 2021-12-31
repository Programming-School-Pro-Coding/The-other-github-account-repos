import turtle

t = turtle.Turtle()
h = turtle.Turtle()
wn = turtle.Screen()

h.color("yellow")
h.hideturtle()
h.penup()

t.penup()
t.goto(-150, -150)
t.pendown()
t.pensize(5)


def square():
    for i in range(4):
        t.forward(30)
        t.left(90)


wn.bgcolor("black")
t.color("White")
h.goto(0, 200)

h.pendown()
for i in range(4):
    t.forward(300)
    t.left(90)
    location = t.pos()
    h.write(f"Turtle's curent position = {location}", align="center")
    square()
    h.clear()