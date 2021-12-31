import turtle
t = turtle.Turtle()

t.color("red", "brown")
t.pensize(5)
t.speed(5)
t.shape("turtle")

for i in range(4):
    t.forward(50)
    t.left(90)
t.forward(50)

h = t.clone()

for i in range(4):
    h.forward(50)
    h.right(90)


a = t.clone()
a.left(90)
a.forward(50)

for i in range(4):
    a.forward(50)
    a.right(90)

s = t.clone()
for w in range(2):
    s.left(90)
    s.forward(50)
for i in range(4):
    s.forward(50)
    s.right(90)

i = t.clone()

for y in range(3):
    i.left(90)
    i.forward(50)
for t in range(4):
    i.forward(50)
    i.right(90)

