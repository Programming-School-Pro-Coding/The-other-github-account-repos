import turtle

Moh = turtle.Turtle()
foo = turtle.Turtle()
M = turtle.Turtle()
xo = turtle.Turtle()
s = turtle.Turtle()
t = turtle.Turtle()
wn = turtle.Screen()

wn.title("Parallelogram shape")
wn.bgcolor("Green")

# pen = t.pensize(8)
# color = t.color("Yellow")
# fillcolor = t.fillcolor("Navy")
# pencolor = t.pencolor("Green")
# shape = t.shape("turtle")
# shapesize = t.shapesize(4)
# speed = t.speed(10)


class Shapes:
    def __init__(self, name_of_the_shape):
        self.name_of_the_shape = name_of_the_shape

    def make_turtle(shapes, speeds, colors, fillcolors, pensizes):
        Moh.shape(shapes)
        Moh.speed(speeds)
        Moh.color(colors)
        Moh.fillcolor(fillcolors)
        Moh.pensize(pensizes)

    def square():
        for i in range(4):
            Moh.forward(100)
            Moh.left(90)

    def triangle():
        for i in range(3):
            Moh.forward(100)
            Moh.left(120)

    def Parallelogram():
        Moh.penup()
        Moh.setx(-100)
        Moh.sety(-100)
        Moh.pendown()

        Moh.forward(200)
        Moh.left(100)
        Moh.forward(150)
        Moh.left(80)
        Moh.forward(150)
        Moh.left(80)
        Moh.forward(150)

    def rectangle():
        for i in [200, 100, 200, 100]:
            Moh.forward(i)
            Moh.left(90)

    def three_squares():
        for i in range(4):
            Moh.forward(100)
            Moh.left(90)

        Moh.forward(40)
        Moh.left(90)
        Moh.forward(50)
        Moh.left(90)

        Moh.forward(40)
        Moh.backward(40)
        Moh.right(90)

        Moh.backward(50)
        Moh.right(90)
        Moh.forward(10)
        Moh.left(90)

        Moh.forward(60)
        Moh.left(90)
        Moh.forward(50)
        Moh.left(180)

        Moh.forward(50)
        Moh.right(90)
        Moh.forward(60)
        Moh.left(90)
        Moh.forward(10)
        Moh.left(90)

        Moh.forward(70)
        Moh.left(90)
        Moh.forward(60)
        Moh.left(180)
        Moh.forward(60)
        Moh.right(90)
        Moh.forward(70)
        Moh.left(90)
        Moh.forward(10)
        Moh.left(90)

        Moh.forward(80)
        Moh.left(90)
        Moh.forward(70)
        Moh.left(180)
        Moh.forward(70)
        Moh.right(90)
        Moh.forward(80)

        Moh.left(90)

        Moh.forward(10)
        Moh.left(90)
        Moh.forward(90)
        Moh.left(90)
        Moh.forward(80)

    def Draw_equal():
        Moh.forward(110)
        Moh.right(90)

        Moh.penup()
        Moh.goto(110, 60)
        Moh.pendown()

        Moh.right(90)
        Moh.forward(110)

    def Hexagon():
        Moh.forward(100)
        Moh.left(50)
        Moh.forward(100)
        Moh.left(50)
        Moh.forward(100)
        Moh.left(50)
        Moh.forward(100)
        Moh.left(50)
        Moh.forward(115)
        Moh.left(50)
        Moh.forward(105)
        Moh.left(60)
        Moh.forward(115)

    def My_first_letter():
        Moh.left(50)
        Moh.forward(100)
        Moh.right(100)
        Moh.forward(50)
        Moh.left(100)
        Moh.forward(50)
        Moh.right(100)
        Moh.forward(100)

    def The_letter_A():
        Moh.left(60)
        Moh.forward(100)
        Moh.right(130)
        Moh.forward(100)
        Moh.backward(50)
        Moh.right(113)
        Moh.forward(40)

    def star():
        Moh.left(90)
        Moh.forward(100)
        Moh.backward(50)
        Moh.right(90)
        Moh.forward(50)
        Moh.backward(50)
        Moh.left(180)
        Moh.forward(50)
        Moh.backward(50)
        Moh.left(50)
        Moh.forward(50)
        Moh.backward(50)
        Moh.backward(50)
        Moh.forward(50)
        Moh.left(80)
        Moh.forward(50)
        Moh.backward(100)

    def three_rectangles():
        M.color(0.955, 0.0, 0.0)

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

        foo.color(0.955, 0.955, 0.0)

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

        coo = xo.xcor()
        xo.penup()
        xo.setx(coo - 200)
        co = xo.ycor()
        xo.sety(co - 100)
        xo.pendown()

        xo.color(0.0, 0.755, 0.0)

        xo.begin_fill()
        xo.forward(400)
        xo.right(90)
        xo.forward(100)
        xo.right(90)
        xo.forward(400)
        xo.right(90)
        xo.forward(100)
        xo.end_fill()

        cooo = Moh.ycor()
        coooo = Moh.xcor()
        s.penup()
        s.sety(cooo - 100)
        s.setx(coooo - 20)
        s.pendown()

        s.begin_fill()
        s.left(50)
        s.forward(30)
        s.right(100)
        s.forward(30)
        s.left(150)
        s.forward(30)
        s.right(50)
        s.forward(30)
        s.left(130)
        s.forward(30)
        s.right(80)
        s.forward(30)
        s.left(160)
        s.forward(30)
        s.right(80)
        s.forward(30)
        s.left(130)
        s.forward(30)
        s.right(40)
        s.forward(30)
        s.end_fill()

    def rectangles():
        xo.color(0.0, 0.755, 0.0)

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
        foo.color(0.955, 0.955, 0.0)

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
        M.color(0.955, 0.0, 0.0)

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

    def red_circle():
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
        t.goto(200.00, 20.00)
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
        t.goto(0, 0)
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

    def the_Water_Melon():
        wn.colormode(255)
        t.color(188, 218, 81)

        t.penup()
        t.sety(50)
        t.setx(50)
        t.pendown()

        t.begin_fill()
        t.right(90)
        t.circle(-100, 180)
        t.left(90)
        t.forward(30)
        t.left(90)
        t.circle(130, 180)
        t.left(90)
        t.forward(30)
        t.end_fill()

        t.fillcolor("red")
        t.begin_fill()
        t.forward(200)
        t.left(90)
        t.circle(100, 180)
        t.end_fill()
        t.penup()
        p = t.xcor()
        t.setx(p - 20)
        x = t.ycor()
        t.sety(x - 20)
        t.pendown()
        t.color("black")
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        t.penup()
        p = t.xcor()
        t.setx(p - 10)
        t.pendown()
        t.color("White")
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()
        p = t.xcor()
        t.setx(p + 30)
        x = t.ycor()
        t.sety(x + 20)
        t.pendown()
        t.left(90)
        t.forward(200)
        t.penup()
        p = t.xcor()
        t.setx(p + 30)
        x = t.ycor()
        t.sety(x - 10)
        t.pendown()
        t.color("black")
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        t.penup()
        z = t.ycor()
        t.sety(z - 5)
        a = t.xcor()
        t.setx(a + 5)
        t.pendown()
        t.color("White")
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()
        t.goto(-55, 0)
        t.left(90)
        t.color("black")
        t.begin_fill()
        t.circle(10, 180)
        t.end_fill()


Shapes("Square")
shape1 = Shapes.make_turtle("turtle", 5, "navy", "blue", 5)

Shapes.square()
Shapes.triangle()
Shapes.Parallelogram()
Shapes.Hexagon()
Shapes.Draw_equal()
Shapes.My_first_letter()
Shapes.rectangles()
Shapes.red_circle()
Shapes.star()
Shapes.the_Water_Melon()
Shapes.three_rectangles()
Shapes.three_squares()
