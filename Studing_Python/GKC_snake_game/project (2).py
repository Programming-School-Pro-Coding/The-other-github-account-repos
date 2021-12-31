import turtle

t = turtle.Turtle()
f = turtle.Turtle()

wn = turtle.Screen()
wn.bgcolor("Black")

t.shape("square")
t.color("orange")


f.shape("circle")
f.color("orange")
f.penup()
f.forward(50)
f.sety(30)
f.pendown()