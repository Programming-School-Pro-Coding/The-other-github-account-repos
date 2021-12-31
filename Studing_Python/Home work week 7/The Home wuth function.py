import turtle

t = turtle.Turtle()


def move_to(go, got=0):

    t.goto(go, got)


def move_to2(gotos):
    t.sety(gotos)


def move_to3(g):
    t.penup()
    t.setx(g)
    t.pendown()


def draw_square():
    for i in range(4):
        t.forward(10)
        t.left(90)


def draw_rectang():
    for i in [200, 120, 200, 120]:
        t.forward(i)
        t.left(90)


def draw_rectang2():
    for i in [30, 40, 30, 40]:
        t.forward(i)
        t.left(90)


def the_home():
    draw_rectang()

    move_to2(120)

    move_to(100, 170)
    move_to(200, 120)

    t.penup()
    move_to(20, 80)
    t.pendown()

    for y in range(3):
        for n in range(4):
            t.left(90)
            draw_square()
        t.penup()
        move_to3(t.xcor() + 80)
        t.pendown()

    t.penup()
    move_to(80, 0)
    t.pendown()

    draw_rectang2()


the_home()
