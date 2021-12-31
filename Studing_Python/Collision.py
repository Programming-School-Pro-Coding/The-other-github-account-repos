import turtle
import time

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()

scr = turtle.Screen()
scr.listen()

t3.speed(0)
t3.fillcolor("blue")
t3.penup()
t3.sety(274)
t3.pendown()

t4.speed(0)
t4.fillcolor("blue")
t4.penup()
t4.sety(250)
t4.pendown()

t5.speed(0)
t5.fillcolor("blue")
t5.penup()
t5.sety(230)
t5.pendown()

scr.bgcolor("Blue")

def write_distance():
    while True:
        dis = t1.distance(t2)
        t3.write(f"Distance between T1 and T2 = {dis}")
        time.sleep(0.1)
        t3.clear()

def write_x_y_cor_of_t1():
    while True:
        cor = t1.pos()
        t4.write(f"position of T1 = {cor}")
        time.sleep(0.1)
        t4.clear()

def write_x_y_cor_of_t2():
    while True:
        cor = t2.pos()
        t5.write(f"position of T2 = {cor}")
        time.sleep(1)
        t5.clear()
def up():
    t1.setheading(90)
    t1.forward(30)
def down():
    t1.setheading(-90)
    t1.forward(30)
def right():
    t1.setheading(0)
    t1.forward(30)
def left():
    t1.setheading(180)
    t1.forward(30)

def Up2():
    t2.setheading(90)
    t2.forward(30)
def down2():
    t2.setheading(-90)
    t2.forward(30)
def right2():
    t2.setheading(0)
    t2.forward(30)
def left2():
    t2.setheading(180)
    t2.forward(30)

scr.onkey(up, "Up")
scr.onkey(down, "Down")
scr.onkey(right, "Right")
scr.onkey(left, "Left")

scr.onkey(Up2, "w")
scr.onkey(down2, "s")
scr.onkey(right2, "d")
scr.onkey(left2, "a")

write_distance()
write_x_y_cor_of_t1()
write_x_y_cor_of_t2()