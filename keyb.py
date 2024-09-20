import turtle
import keyboard
import random


win = turtle.Screen()
win.setup(width=600, height=600)
win.bgcolor("black")

t = turtle.Turtle()
t.color("white")


def goUp():
    t.forward(100)


def goDown():
    t.backward(100)


def goLeft():
    t.left(50)


def goRight():
    t.right(50)


def goSpace():
    t.color(random.random(), random.random(), random.random())

win.listen()
win.onkey(goUp, "Up")
win.onkey(goDown, "Down")
win.onkey(goLeft, "Left")
win.onkey(goRight, "Right")
win.onkey(goSpace, "space")

turtle.done()