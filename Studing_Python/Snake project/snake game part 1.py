import turtle

# creation of the game bored
wn = turtle.Screen()
wn.bgcolor("Black")
wn.setup(700, 700)
wn.title("Snake Game G.K.C")

# Snake head object
head = turtle.Turtle("square")
head.color("Green")
head.speed(0)
head.penup()

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