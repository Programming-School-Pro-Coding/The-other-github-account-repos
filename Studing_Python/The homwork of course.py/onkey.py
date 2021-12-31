import turtle

t = turtle.Turtle()
wn = turtle.Screen()
wn.listen()

def square():
    t.pensize(7)
    t.color("blue")
    for i in range(4):
        t.forward(100)
        t.left(90)
    

def rectangle():
    t.pensize(6)
    t.color("navy")
    for i in range(2):
        t.forward(200)
        t.left(90)
        t.forward(100)
        t.left(90)

def triangle():
    t.pensize(5)
    t.color("yellow")
    for i in range(3):
        t.forward(100)
        t.left(120)

wn.onkey(square, "s")
wn.onkey(t.clear, "space")
wn.onkey(rectangle, "r")
wn.onkey(triangle, "t")