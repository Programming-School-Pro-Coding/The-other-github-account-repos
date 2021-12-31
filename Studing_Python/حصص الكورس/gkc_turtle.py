import turtle

t = turtle.Turtle()


class gkc_turtle():

    def make_turtle(shapes, speeds, colors, fillcolors, pensizes):
        t.shape(shapes)
        t.speed(speeds)
        t.color(colors)
        t.fillcolor(fillcolors)
        t.pensize(pensizes)

    def make_screen(titles, bgcolors):
        wn.title(titles)
        wn.bgcolor(bgcolors)


gkc_turtle.make_turtle("turtle", 4, "navy", "blue", 5)
t.forward(1000)
