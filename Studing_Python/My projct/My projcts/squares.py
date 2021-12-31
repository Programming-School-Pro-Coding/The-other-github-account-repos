import turtle

t = turtle.Turtle()
t.pensize(5)

for i in [["red", 200], ["yellow", 120], ["navy",200], ["blue", 120]]:
    t.color(i[1])
    t.forward(i[0])
    t.left(90)