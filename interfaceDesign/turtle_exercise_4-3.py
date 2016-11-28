# This is the 4.3 exercise with the 'turtle' module

import turtle

def square(t, length):
    t = turtle.Turtle()
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, n):
    t = turtle.Turtle()
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t, r):
    t = turtle.Turtle()
    circumference = polygon(2, 10, 30)
    for i in range(r):
        t.fd(circumference)
        t.lt(360/n)


square(2, 200)
polygon(2, 3, 20)
circle(2, 20)
