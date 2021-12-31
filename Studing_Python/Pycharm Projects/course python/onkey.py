import turtle

t = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("black")
t.color("White")

for i in range(4):
    t.forward(250)
    t.left(90)
    for i in range(4):
        t.forward(50)
        t.left(90)