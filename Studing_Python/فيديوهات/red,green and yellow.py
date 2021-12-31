import turtle

t = turtle.Turtle()
t.color("navy")
t.pensize(6)
t.shapesize(5)

t.forward(133.5)
t.right(156)
t.forward(153)
t.backward(53)
t.left(63)
t.forward(158)

coo = t.ycor()
t.sety(coo + 20)
print(t.pos())





