from hashlib import new
import turtle
from random import randint
from time import sleep

# Creation og game board
wn = turtle.Screen()
wn.title("Snake Game G.K.C")
wn.setup(width=700, height=700)
wn.bgcolor('black')
wn.tracer(0)



# Snake's Head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('green')
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake body
body_parts = []

# fruit object
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("circle")
fruit.color("red")
fruit.penup()
fruit.goto(80,50)
fruit.shapesize(0.6)

# score turtle object
writer = turtle.Turtle()
writer.speed(0)
writer.color('white')
writer.hideturtle()
writer.penup()
scores = [0, 0]

writer.goto(-100, 325)
writer.write(f"Score: {scores[0]}",align="right", font=("Comic Sans MS",15,"normal"))

writer.goto(100, 325)
writer.write(f"High Score: {scores[1]}",align="right", font=("Comic Sans MS",15,"normal"))

def move():
          px = 21
          if head.direction == "up":
                    head.setheading(90)
                    head.forward(px)
          if head.direction == "down":
                    head.setheading(270)
                    head.forward(px)
          if head.direction == "right":
                    head.setheading(0)
                    head.forward(px)
          if head.direction == "left":
                    head.setheading(180)
                    head.forward(px)

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

# Score function
def scoring():
          if head.distance(fruit) < 16:
                    writer.clear()
                    scores[0] += 10
                    if scores[0] > scores[1] :
                              scores[1] = scores[0]
                              fruit.goto(randint(-290, 290), randint(-290, 290))

                    # adding new parts of snake's body
                    new_part = turtle.Turtle()
                    new_part.speed(0)
                    new_part.color("red")
                    new_part.shape("square")
                    new_part.penup()
                    body_parts.append(new_part)

                    writer.goto(-100, 325)
                    writer.write(f"Score: {scores[0]}",align="right", font=("Comic Sans MS",15,"normal"))

                    writer.goto(100, 325)
                    writer.write(f"High Score: {scores[1]}",align="right", font=("Comic Sans MS",15,"normal"))

# borders collision
def borders_colli():
          if head.xcor() > 335 or head.xcor() < -335 or head.ycor() < -335:
                    sleep(1)
                    scores[0] = 0
                    head.direction = "stop"
                    writer.clear()
                    head.goto(0, 0)

# [0,1,2,3,4,5,6,7,8,9,10,11]
#snake body controll
def snake_body():
          last_index = len(body_parts) - 1
          for i in range(last_index,0,-1):
                    x = body_parts[i -1].xcor()
                    y = body_parts[i -1].ycor()

          if len(body_parts) > 0:
                    body_parts[0].goto(head.xcor(), head.ycor())


# keyboard bingins
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_right, "Right")
wn.onkey(go_left, "Left")

while True:
          wn.update()
          sleep(0.1)
          scoring()
          snake_body()
          move()
          borders_colli()

turtle.done()