from turtle import *
speed(0)
colors = ['red', 'purple', 'blue', 'green', 'orange']
for x in range(150):
    pencolor(colors[x % 5])
    width(x/10 + 1)
    forward(x)
    left(59)
