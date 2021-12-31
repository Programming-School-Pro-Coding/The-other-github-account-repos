import turtle

l = turtle.Turtle()
wn = turtle.Screen()



wn.colormode(255)
l.color(255, 0, 0)
l.begin_fill()
for i in range(100):
    l.forward(35)
    l.left(90)
    l.forward(17.5)
    l.left(90)
    l.forward(40)
    l.left(45)
l.end_fill()