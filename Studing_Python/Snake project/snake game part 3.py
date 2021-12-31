import turtle
from random import randint
from time import sleep

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
fruit.speed(0)
fruit.shapesize(0.6)
fruit.color("red")
fruit.penup()
fruit.goto(80, 50)

# Writing score and High score
Writer = turtle.Turtle()
scores = [0, 0]
Writer.color("White")

Writer.penup()
Writer.hideturtle()
Writer.speed(0)

Writer.goto(-100, 300)
Writer.write(f"Score : {scores[0]}", align="right", font=("Comic Sans MS", 15, "normal"))

Writer.goto(100, 300)
Writer.write(f"High Score : {scores[1]}", align="left", font=("Comic Sans MS"
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
    forward_with_pixels = 5
    if head.direction == "up":
        head.setheading(90)
        head.forward(forward_with_pixels)

    if head.direction == "down":
        head.setheading(270)
        head.forward(forward_with_pixels)

    if head.direction == "right":
        head.setheading(0)
        head.forward(forward_with_pixels)

    if head.direction == "left":
        head.setheading(180)
        head.forward(forward_with_pixels)

wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_right, "Right")
wn.onkey(go_left, "Left")

def scoring():
    if head.distance(fruit) < 16:
        Writer.clear()
        scores[0] += 10
        fruit.goto(randint(-335, 335), randint(-335, 335))
        if scores[1] < scores[0]:
            scores[1] = scores[0]

        Writer.goto(-100, 300)
        Writer.write(f"Score : {scores[0]}", align="right", font=("Comic Sans MS", 15, "normal"))

        Writer.goto(100, 300)
        Writer.write(f"High Score : {scores[1]}", align="left", font=("Comic Sans MS" , 15, "normal"))

def border_collision():
    if head.xcor() > 335 or head.xcor() < -335 or head.ycor() < -335 or head.ycor() > 335:
        sleep(0.5)
        scores[0] = 0
        Writer.clear()
        head.direction = "stop"
        head.goto(0, 0)
        scores[1] == scores[1]

        Writer.goto(-100, 300)
        Writer.write(f"Score : {scores[0]}", align="right", font=("Comic Sans MS", 15, "normal"))

        Writer.goto(100, 300)
        Writer.write(f"High Score : {scores[1]}", align="left", font=("Comic Sans MS" , 15, "normal"))

# game main loop
while True:
    wn.update()
    move()
    scoring()
    border_collision()