import turtle

t = turtle.Turtle()
wn = turtle.Screen()

wn.title("Parallelogram shape")
wn.bgcolor("Green")
wn.setup(width=700, height=700)

pen = t.pensize(8)
color = t.color("Yellow")
fillcolor = t.fillcolor("Navy")
pencolor = t.pencolor("Green")
shape = t.shape("turtle")
shapesize = t.shapesize(4)
speed = t.speed(10)


class Shapes:
    def __init__(self, name_of_the_shape):
        self.name_of_the_shape = name_of_the_shape

    def square(self, distance, angle, speed, shapesize, shape, pencolor, color, fillcolor, pen):
        t.speed(speed)
        t.shapesize(shapesize)
        t.shape(shape)
        t.pencolor(pencolor)
        t.fillcolor(color)
        t.color(fillcolor)
        t.pensize(pen)
        for i in range(4):
            t.forward(distance)
            t.left(angle)

    def rectangle(self, angle, speed, shapesize, shape, pencolor, fillcolor, color, pen):
        t.speed(speed)
        t.shapesize(shapesize)
        t.shape(shape)
        t.pencolor(pencolor)
        t.fillcolor(fillcolor)
        t.color(color)
        t.pensize(pen)
        for i in [200, 100, 200, 100]:
            t.forward(i)
            t.left(angle)

    def triangle(self, distance, speed, shapesize, shape, pencolor, fillcolor, color, pen=9, angle=50):
        t.speed(speed)
        t.shapesize(shapesize)
        t.shape(shape)
        t.pencolor(pencolor)
        t.fillcolor(fillcolor)
        t.color(color)
        t.pensize(pen)
        for i in range(3):
            t.forward(distance)
            t.left(50)


Shapes.triangle(100, 10, 5, "square", "blue", "navy", "yellow")
