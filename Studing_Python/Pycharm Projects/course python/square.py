import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("Black")

# properties
t.color("white")
t.shape("turtle")
t.pensize(5)

# x y coordinates
t.penup()
t.goto(-120, -50)
t.pendown()
# for loop square and write a sentence on the screen
for i in range(4):
    t.forward(250)
    t.left(90)
    p = t.pos()
    t.write(p, align="center")
    for k in range(4):
        t.forward(25)
        t.left(90)