import turtle
t = turtle.Turtle()
a = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")

# properties
t.color("white")
t.shape("turtle")
t.pensize(5)

t.penup()
t.goto(-80, -50)
t.pendown()

for i in range(4):
    t.forward(200)
    t.left(90)
    t.clear()
    p = t.pos()
    t.write(p, align="center", font=("Arial", 11, "normal"))
    for k in range(4):
        t.forward(25)
        t.left(90)
