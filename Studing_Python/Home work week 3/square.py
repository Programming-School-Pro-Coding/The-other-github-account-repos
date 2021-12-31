import turtle

ko = turtle.Turtle()

color = "navy"
pen_size = 5
shape = "circle"
shape_size = 2
speed = 6
side_length = 100
Angle = 90

ko.color(color)
ko.pensize(pen_size)
ko.shape(shape)
ko.shapesize(shape_size)
ko.speed(speed)

for x in range(4):
    ko.forward(side_length)
    ko.left(Angle)

ko.penup()
ko.right(140)
ko.forward(30)
ko.pendown()

ko.right(130)

color = "navy"
pen_size = 4
shape = "triangle"
shape_size = 3
speed = 7
side_length = 150
Angle = 90

ko.color(color)
ko.pensize(pen_size)
ko.shape(shape)
ko.shapesize(shape_size)
ko.speed(speed)

for v in range(4):
    ko.forward(side_length)
    ko.right(Angle)

ko.penup()
ko.left(130)
ko.forward(30)
ko.pendown()

ko.right(130)

color = "navy"
pen_size = 4
shape = "rectangle"
shape_size = 1
speed = 8
side_length = 200
Angle = 90



for v in range(4):
    ko.forward(side_length)
    ko.right(Angle)

ko.penup()
ko.left(130)
ko.forward(30)
ko.pendown()

ko.right(130)

color = "navy"
pen_size = 4
shape = "square"
shape_size = 3
speed = 8
side_length = 250
Angle = 90



for v in range(4):
    ko.forward(side_length)
    ko.right(Angle)

ko.penup()
ko.left(130)
ko.forward(30)
ko.pendown()

ko.right(130)

color = "navy"
pen_size = 4
shape = "circle"
shape_size = 5
speed = 8
side_length = 300
Angle = 90



for v in range(4):
    ko.forward(side_length)
    ko.right(Angle)
