
from turtle import *

print("ax^2 + bx + c\n\njust click enter if there is not one\n\n\n")

def turtleSettings():

    hideturtle()
    bgcolor("lightblue")
    speed("fastest")
    print("aX^2\n\n\n")

    setpos(-99,0)
    setpos(99, 0)
    setpos(0, 0)
    setpos(0, 99)
    setpos(0, -99)
    setpos(0, 0)

def Quad():

    xmin = -100
    xmax = 100

    a = input("a = ")
    a = float(a)
    b = input("b = ")
    c = input("c = ")
    turtleSettings()

    if b == "" and c == "":

        penup()
        setpos(xmin, (a*xmax*xmax))
        pendown()
        pensize(2)
        color("red")
        for y in range(xmin, xmax):
            ysqr = (y*y)
            setpos(y, a*ysqr)
            print(ysqr)
        done()
    elif b == "":
        c = float(c)
        penup()
        setpos(xmin, ((a*xmax*xmax)+c))
        pendown()
        pensize(2)
        color("red")
        for y in range(xmin, xmax):
            ysqr = (y*y)
            setpos(y, (a*ysqr)+c)
            print(ysqr)
        done()
    elif c == "":
        b = float(b)
        penup()
        setpos(xmin, ((a*((-b/2c)-xmax)*((-b/2c)-xmax))))
        pendown()
        pensize(2)
        color("red")
        for y in range(xmin, xmax):
            ysqr = (y*y)
            setpos(y, (a*ysqr)+(b*y))
            print(ysqr)
        done()

Quad()
