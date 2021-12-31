import turtle
s = turtle.Screen()
s.bgcolor("navy")



ko = turtle.Turtle()
pretty_color = "yellow"

ko.color(pretty_color)

for side in range(4):
    ko.forward(100)
    ko.right(90)

ba = turtle.Turtle()
ba.color(pretty_color)
for side in range(5) :
    ba.forward(100)
    ba.left(72)
ba.left(105)

foo = turtle.Turtle()
foo.color(pretty_color)
for side in range(3) :
    foo.forward(100)
    foo.left(120)
foo.left(200)
for i in range(3):
    print("The loop was finish")