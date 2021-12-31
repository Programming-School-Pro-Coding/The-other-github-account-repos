import turtle
pen1 = turtle.Turtle()
pen2 = turtle.Turtle()
paper = turtle.Screen()

for i in range(6):
    pen1.forward(100)
    pen1.right(45)

#x = pen1.distance(0, 0)
for i in range(6):
   pen2.forward(100)
   pen2.left(45)

x = pen1.distance(pen2)
print(x)

pen1.forward(341.4213562373096)