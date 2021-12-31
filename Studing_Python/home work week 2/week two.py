import turtle

t = turtle.Turtle()
pen_width = 8
My_shape = "turtle"
My_favorite_speed = 2
My_favorite_color = "navy"
side_length = 150
Angle = 90

t.pensize(pen_width)
t.shape(My_shape)
t.speed(My_favorite_speed)
t.pencolor(My_favorite_color)

for d in range(4):
    t.forward(side_length)
    t.left(Angle)