import turtle



no_side =  int(input("Enter number of sides : "))
side = int(input("Enter the side length : "))
side_color = input("Enter the side color : ")
fill_color = input("Enter the fill color : ")
angle = 360 / no_side

t = turtle.Turtle()
t.color(side_color, fill_color)
t.begin_fill()
for x in range(no_side):
    t.forward(side)
    t.left(angle)
t.end_fill()
t.hideturtle()


print("The code is finish user")