# Turtle

import turtle

t = turtle.Turtle()
class Shapes:
    def square():
            for i in range(4):
                        t.forward(100)
                        t.left(90)

    def triangle():
            for i in range(3):
                        t.forward(100)
                        t.left(72)

    def rectangle():
            for i in [200, 100, 200, 100]:
                        t.forward(i)
                        t.left(90)

    def Three_Squares():
            for i in range(3):
                        for i in range(4):
                                t.forward(100)
                                t.left(90)
                        for i in range(1):
                                t.left(10)

    def Three_Squares1():
            t.speed(0)
            for i in range(29):
                        for i in range(4):
                                t.forward(100)
                                t.left(90)
                        for i in range(1):
                                t.left(10)

    def Three_Rectangles():
            t.speed(0)
            for i in range(3):
                        for i in [200, 100, 200, 100]:
                                t.forward(i)
                                t.left(90)
                        for i in range(1):
                                t.left(10)

    def Three_Rectangles1():
            t.speed(0)
            for i in range(34):
                        for i in [200, 100, 200, 100]:
                                t.forward(i)
                                t.left(90)
                        for i in range(1):
                                t.left(10)

# compares

def replace_vowels(word, char):
    f = ""
    for letter in word:
        if letter in "AEIOUaeiou":
            f += char
        else:
            f += letter
    return f
