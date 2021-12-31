import turtle

t = turtle.Turtle()

t.color("Green")
t.speed(1)
t.shape("triangle")
t.pensize(1)

t.penup()
t.backward(100)
t.pendown()

for i in range(2):
    t.forward(200)
    t.left(90)

h = t.clone()

for n in range(2):
    t.forwward(200)
    t.left(90)