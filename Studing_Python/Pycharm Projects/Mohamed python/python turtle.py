import turtle

# variables
color = "yellow"
Screen_color = "navy"
speed = 5
pen_size = 5
shape = "turtle"
shape_size = 3
side_length = 200
Angle = 90

screen = turtle.Screen()
screen.bgcolor(Screen_color)
foo = turtle.Turtle()
foo.color(color)
foo.pensize(pen_size)
foo.speed(speed)
foo.shape(shape)
foo.shapesize(shape_size)

for n in range(4):
    foo.forward(side_length)
    foo.left(Angle)

