import turtle
t = turtle.Turtle()
scr = turtle.Screen()
scr.listen()

def thick_circle():
    t.pensize(8)
    t.circle(50)

def thin_circle():
    t.pensize(2)
    t.circle(25)

scr.onkey(thick_circle, "e")
scr.onkey(thin_circle, "h")

