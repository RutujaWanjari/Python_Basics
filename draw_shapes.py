# This program demonstrates how to draw different shapes in python

import turtle

window = turtle.Screen()
window.bgcolor("Red")
brad = turtle.Turtle()
brad.color("Yellow")
brad.shape("turtle")
brad.speed(3)


def square():
    for i in range(0, 4):
        brad.forward(100)
        brad.right(90)


def circle():
    brad.circle(50)


def triangle():
    brad.left(180)

    for j in range(0, 3):
        brad.forward(100)
        brad.left(120)


def art():
    brad.right(20)
    brad.color("Red")
    brad.forward(300)
    brad.color("Yellow")

    for i in range(0, 36):
        brad.right(10)
        square()

square()
circle()
triangle()
art()

window.exitonclick()
