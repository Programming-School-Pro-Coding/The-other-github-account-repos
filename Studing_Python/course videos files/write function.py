import turtle
t = turtle.Turtle()
s = turtle.Screen()
t.speed(1)

t.color("red", "brown")
t.pensize(5)
t.shape("turtle")

t.penup()
t.goto(100, 100)
t.pendown()
p = t.pos()

t.write(p, move=False, align="right", font="Arial")