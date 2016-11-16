# This is the 4.3 exercise with the 'turtle' module

import turtle

def square(t, length):
    t = turtle.Turtle()
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, n):
    bob = turtle.Turtle()
    for i in range(n):
        bob.fd(length)
        bob.lt(360/n)

# def circle(t, r):



square(2, 200)
polygon(2, 3, 20)
circle()
