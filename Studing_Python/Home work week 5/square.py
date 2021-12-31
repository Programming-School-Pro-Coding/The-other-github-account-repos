import turtle

# turtle and screen variables
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("Black")

# properties
t.color("white")
t.shape("turtle")
t.pensize(5)

# x y coordinates
t.penup()
t.goto(-80, -50)
t.pendown()
# for loop square and write a sentence on the screen
for i in range(4):
    t.forward(200)
    t.left(90)
    for l in range(4):
        t.clear()
        p = t.pos()
        t.write(p, align="center")
    for k in range(4):
        t.forward(25)
        t.left(90)