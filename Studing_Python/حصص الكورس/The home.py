import turtle

t = turtle.Turtle()
for i in [200, 120, 200, 120]:
    t.forward(i)
    t.left(90)

t.sety(120)
t.goto(100, 170)
t.goto(200, 120)

t.penup()
t.goto(20, 80)
t.pendown()

for y in range(3):
    for n in range(4):
        t.left(90)
        for i in range(4):
            t.forward(10)
            t.left(90)
    t.penup()
    t.setx(t.xcor() + 80)
    t.pendown()

t.penup()
t.goto(80, 0)
t.pendown()

for i in [30, 40, 30, 40]:
    t.forward(i)
    t.left(90)