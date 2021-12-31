import turtle

t = turtle.Turtle()
s = turtle.Screen()

t.color("red", "brown")
t.pensize(5)
t.shape("turtle")

t.penup()
t.goto(100, 100)
t.pendown()
for i in range(4):
    t.forward(100)
    t.left(90)

t.write("Mohamed is ", align="right", font="Arial")
