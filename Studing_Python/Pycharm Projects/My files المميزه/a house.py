import turtle

Moh = turtle.Turtle()


Moh.color(0.1000,0.1000,0.1155)


Moh.penup()

e = Moh.xcor()
Moh.setx(e - 300)
s = Moh.ycor()
Moh.sety(s - 250)

Moh.pendown()

Moh.begin_fill()
Moh.forward(600)
Moh.left(90)
Moh.forward(250)
Moh.left(90)
Moh.forward(600)
Moh.left(90)
Moh.forward(250)
Moh.left(90)
Moh.end_fill()


Moh.color(0.0, 0.955, 0.0)


Moh.begin_fill()
Moh.forward(270)
Moh.left(90)
Moh.forward(100)
Moh.right(90)
Moh.forward(50)
Moh.right(90)
Moh.forward(100)
Moh.end_fill()


k = turtle.Turtle()

k.penup()

a = k.xcor()
k.setx(a - 300)
k.pendown()


k.color(0.255, 0.0, 0.0)

k.begin_fill()
k.left(40)
k.forward(400)
k.right(81.5)
k.forward(390)
k.end_fill()

