# Importing needed modules
import turtle
from typing import Set

# Build your Drawer set drawer's attribities
t = turtle.Turtle()
t.pensize(5)
t.color("navy")

# Build screen object set screen's attribities
scr = turtle.Screen()
scr.listen()

# define functions basic arrows
def Up():
    t.setheading(90)
    t.forward(30)
def down():
    t.setheading(-90)
    t.forward(30)
def right():
    t.setheading(0)
    t.forward(30)
def left():
    t.setheading(180)
    t.forward(30)
# define functions clear, reset, undo

def reset_drawer():
    t.penup()
    t.home()
    t.pendown()

# define functions rotate, go
def rotate():
    t.left(16)
def go():
    t.forward(20)
# key binding
scr.onkey(Up, "Up")
scr.onkey(down, "Down")
scr.onkey(right, "Right")
scr.onkey(left, "Left")
scr.onkey(t.clear, "space")
scr.onkey(reset_drawer, "0")
scr.onkey(t.undo, "u")
scr.onkey(rotate, "plus")
scr.onkey(go, "g")