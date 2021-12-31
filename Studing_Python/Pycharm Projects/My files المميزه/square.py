import turtle


ko = turtle.Turtle()

color = "navy"
pen_size = 5
shape = "circle"
shape_size = 2
speed = 6
side_length = 100
Angle = 90

ko.color("navy")
ko.pensize(5)
ko.shape("circle")
ko.shapesize(2)
ko.speed(6)

for x in range(4):
    ko.forward(100)
    ko.left(90)

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

ko.color("navy")
ko.pensize(4)
ko.shape("triangle")
ko.shapesize(3)
ko.speed(7)

for v in range(4):
    ko.forward(150)
    ko.right(90)