import turtle
import random

# creation of the game bored
wn = turtle.Screen()
wn.listen()
wn.bgcolor("Black")
wn.setup(700, 700)
wn.title("Snake Game G.K.C")

# Snake head object
head = turtle.Turtle("square")
head.color("Green")
head.speed(0)
head.penup()
head.direction = "stop"

# fruit object
fruit = turtle.Turtle("circle")
fruit.shapesize(0.6)
fruit.color("red")
fruit.penup()
fruit.goto(80, 50)

# Writing score and High score
Writer = turtle.Turtle()
Writer.color("White")

Writer.penup()
Writer.hideturtle()
Writer.speed(0)

Writer.goto(-100, 300)
Writer.write("Score : 0", align="right", font=("Comic Sans MS", 15, "normal"))

Writer.goto(100, 300)
Writer.write("High Score : 0", align="left", font=("Comic Sans MS"
, 15, "normal"))

# Direction functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_left():
    if head.direction != "right":
        head.direction = "left"

# move function
def move():
    if head.direction == "up":
        head.setheading(90)
        head.forward(3)

    if head.direction == "down":
        head.setheading(270)
        head.forward(3)

    if head.direction == "right":
        head.setheading(0)
        head.forward(3)

    if head.direction == "left":
        head.setheading(180)
        head.forward(3)

wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_right, "Right")
wn.onkey(go_left, "Left")


def fruit_control():
    if head.distance(fruit) < 16:
        x = random.randint(-335, 335)
        y = random.randint(-335, 335)
        fruit.goto(x, y)

# game main loop
while True:
    wn.update()
    move()
    fruit_control()