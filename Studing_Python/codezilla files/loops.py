import turtle

x = 5

while x < 10:
    print(x)
    x += 1

for i in range(10):
    print(x)
    x += 2

k = turtle.Turtle()

# Draw square
for i in range(4):
    k.forward(250)
    k.left(90)

o = turtle.Turtle()

# Draw square
for i in range(2):
    o.forward(300)
    o.left(90)
    o.forward(125)
    o.left(90)