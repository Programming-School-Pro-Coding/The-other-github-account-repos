import turtle

t = turtle.Turtle()
t.penup()

wn = turtle.Screen()
wn.bgcolor("Black")
t.color("Green")
wn.listen()

t.direction = "stop"

# stop >> "stop"
# up >> "fo2"
# down >> "ta7t"
# right >> "ymeen"
# left >> "yaser"

def go_up():
    if t.direction != "Ta7t":
        t.direction = "fo2"

def go_right():
    if t.direction != "yaser":
        t.direction = "ymeen"

def go_down():
    if t.direction != "fo2":
        t.direction = "ta7t"

def go_left():
    if t.direction != "ymeen":
        t.direction = "yaser"

def move():
    if t.direction == "fo2":
        t.setheading(90)
        t.forward(3)

    if t.direction == "ta7t":
        t.setheading(270)
        t.forward(3)

    if t.direction == "ymeen":
        t.setheading(0)
        t.forward(3)

    if t.direction == "yaser":
        t.setheading(180)
        t.forward(3)


wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_right, "Right")
wn.onkey(go_left, "Left")

while True:
    wn.update()
    move()