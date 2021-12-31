import turtle

t = turtle.Turtle()
wn = turtle.Screen()


def make_turtle(shapes, speeds, colors, fillcolors, pensizes):
    t.shape(shapes)
    t.speed(speeds)
    t.color(colors)
    t.fillcolor(fillcolors)
    t.pensize(pensizes)


def make_screen(titles, bgcolors):
    wn.title(titles)
    wn.bgcolor(bgcolors)


wn = make_screen("GKC Playground", "yellow")

n = make_turtle("triangle", 3, "navy", "red", 4)

for i in range(4):
    t.forward(100)
    t.left(90)
