import turtle
import time

wn = turtle.Screen()

wn.title("Animation with python")
wn.bgcolor("black")

player = turtle.Turtle()
player.color('White')
def player_animate():
    if player.shape() == "circle":
        player.shape("square")
    elif player.shape() == "square":
        player.shape("circle")

    wn.ontimer(player_animate, 500)

player_animate()

while True:
    wn.update()
    print("Game")