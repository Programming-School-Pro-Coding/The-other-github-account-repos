import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(7)

t.circle(20)

t.penup()
t.sety(-30)
t.pendown()

t.circle(50)
t.circle(50, 90)
t.penup()
t.setx(200)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(200, 180)
t.end_fill()

t.right(90)

t.penup()
t.goto(200.00,20.00)
t.pendown()
t.left(90)

t.circle(-200, 180)
t.color("black")

t.right(90)
t.forward(150)
t.penup()
t.forward(100)
t.pendown()
t.forward(150)

t.left(90)
t.circle(200, 180)

t.penup()
t.goto(0,0)
t.pendown()
t.right(90)

t.fillcolor("White")

t.penup()
t.sety(-30)
t.pendown()
t.begin_fill()
t.circle(-50)
t.end_fill()

t.penup()
t.sety(1)
t.pendown()

t.begin_fill()
t.circle(-20)
t.end_fill()

t.penup()
t.sety(20)
t.setx(200)
t.pendown()
t.left(90)
t.circle(-200, 180)