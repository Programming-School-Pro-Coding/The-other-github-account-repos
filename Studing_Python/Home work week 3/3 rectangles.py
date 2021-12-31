import turtle

xo = turtle.Turtle()

xo.color(0.0 , 0.755 , 0.0)

xo.begin_fill()
xo.forward(100)
xo.left(90)
xo.forward(200)
xo.left(90)
xo.forward(100)
xo.left(90)
xo.forward(200)
xo.end_fill()

foo = turtle.Turtle()
foo.color(0.955,0.955,0.0)

coo = foo.xcor()
foo.penup()
foo.setx(coo + 100)
foo.pendown()

foo.begin_fill()
foo.forward(100)
foo.left(90)
foo.forward(200)
foo.left(90)
foo.forward(100)
foo.end_fill()

M = turtle.Turtle()
M.color(0.955,0.0,0.0)

coo = M.xcor()
M.penup()
M.setx(coo + 200)
M.pendown()

M.begin_fill()
M.forward(100)
M.left(90)
M.forward(200)
M.left(90)
M.forward(100)
M.end_fill()