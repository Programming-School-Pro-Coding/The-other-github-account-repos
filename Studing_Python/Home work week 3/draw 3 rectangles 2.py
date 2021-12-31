import turtle




M = turtle.Turtle()
M.color(0.955,0.0,0.0)

M.penup()
coo = M.xcor()
M.setx(coo - 200)
M.pendown()

M.begin_fill()
M.forward(400)
M.left(90)
M.forward(100)
M.left(90)
M.forward(400)
M.end_fill()



foo = turtle.Turtle()
foo.color(0.955,0.955,0.0)

coo = foo.xcor()
foo.penup()
foo.setx(coo - 200)
foo.pendown()

foo.begin_fill()
foo.forward(400)
foo.right(90)
foo.forward(100)
foo.right(90)
foo.forward(400)
foo.end_fill()

xo = turtle.Turtle()


coo = xo.xcor()
xo.penup()
xo.setx(coo - 200)
co = xo.ycor()
xo.sety(co - 100)
xo.pendown()

xo.color(0.0 , 0.755 , 0.0)

xo.begin_fill()
xo.forward(400)
xo.right(90)
xo.forward(100)
xo.right(90)
xo.forward(400)
xo.right(90)
xo.forward(100)
xo.end_fill()

Moh = turtle.Turtle()

cooo = Moh.ycor()
coooo = Moh.xcor()
Moh.penup()
Moh.sety(cooo - 100)
Moh.setx(coooo - 20)
Moh.pendown()

Moh.begin_fill()
Moh.left(50)
Moh.forward(30)
Moh.right(100)
Moh.forward(30)
Moh.left(150)
Moh.forward(30)
Moh.right(50)
Moh.forward(30)
Moh.left(130)
Moh.forward(30)
Moh.right(80)
Moh.forward(30)
Moh.left(160)
Moh.forward(30)
Moh.right(80)
Moh.forward(30)
Moh.left(130)
Moh.forward(30)
Moh.right(40)
Moh.forward(30)
Moh.end_fill()





