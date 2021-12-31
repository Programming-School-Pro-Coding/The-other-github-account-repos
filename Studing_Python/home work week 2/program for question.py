import turtle

print("We can draw a triangle for you")
print("_" * 25)

sides = input("How many sides ? ")

The_Length = input("what is the side length ?: ")

The_Angle = input("what is the side Angle ?: ")

The_color = input("What is the color of the sides ?: ")

The_fill_color = input("Which color you want to fill your shape with ?: ")

# The triangle

Moh = turtle.Turtle()
Moh.speed(2)
Moh.width(10)
Moh.pensize(5)

#properties
Moh.color(The_color, The_fill_color)
Moh.shape("turtle")

#The 4 main commands

Moh.begin_fill()
for i in range(sides):
    Moh.forward(The_Length)
    Moh.left(The_Angle)
Moh.endfill()