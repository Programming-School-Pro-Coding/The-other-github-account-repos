import turtle
import random

t = turtle.Turtle()
wn = turtle.Screen()
wn.setup(750, 750)
wn.colormode(255)
wn.bgcolor(0, 0, 30)
t.color(211, 159, 0)
t.speed(5)



for m in range(50):
    x_num = random.randint(-375, 375)
    y_num = random.randint(-375, 375)
    t.begin_fill()
    for i in range(5):
        t.forward(20)
        t.right(144)
    t.end_fill()
    t.penup()
    t.goto(x_num, y_num)
    t.pendown()