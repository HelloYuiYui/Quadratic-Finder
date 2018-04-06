
#EIA, twwsts, 3 April 2018.
#This a program for to draw quadratic functions. It also gives the roots of the parabola.

from turtle import *
import math

print("ax^2 + bx + c\n\njust click enter if there is not one\n\n\n")

def turtleSettings():

    #general settings.
    hideturtle()
    bgcolor("lightblue")
    speed("fastest")
    title("Parabola Creator")

    #drawing the x and y axes.
    setpos(-99,0)
    setpos(99, 0)
    setpos(0, 0)
    setpos(0, 99)
    setpos(0, -99)
    setpos(0, 0)

def Quad():    

    #the values to draw a parabola between.
    xmin = -100
    xmax = 100

    #values of the parabola.
    a = input("a = ")
    b = input("b = ")
    c = input("c = ")

    #the code does not work proper if there is a value between 1 and -1 for the variable a. 
    while type(a) is str:
        try:
            a = float(a)
            break
        except ValueError:
            print("-a- is not valid.")
            a = input("enter a new value for a: ")
            print("value is not valid")

    #to open the turtle window.
    turtleSettings()

    #for a parabola with a formula in -ax^2- form.    
    if b == "" and c == "":

        #root, axis of symetry and y-intercept.
        print("\n\nthe root and y-intercept for this parabola is 0")
        print("axis of symetry is x = " + (-b/(2*a)) + "\n")

        #setting the position of the pen to the starting point.
        penup()
        setpos(xmin, (a*xmax*xmax))
        pendown()
        pensize(2)
        color("red")

        #to draw every coordinate between the range.
        for y in range(xmin, xmax):
            ysqr = (y*y)
            setpos(y, a*ysqr)
        done()

    #for a parabola with a formula like -ax^2+c-
    elif b == "":
        c = float(c)
        b = 0

        #to find roots, axis of symetry and y-intercept
        if b**2-4*a*c >= 0:
            root1 = ((-b - (math.sqrt(b**2-4*a*c)))/2*a)
            root2 = ((-b + (math.sqrt(b**2-4*a*c)))/2*a)
            print("\n\nroots are " + str(root1) + " and " + str(root2))
        else:
            print("\n\nthere is no roots for this parabola")
        yintercept = c
        print("\ny-intercept is " + str(c) + "\n")   
        print("axis of symetry is x = " + (-b/(2*a)) + "\n")

        #setting the position of the pen to the starting point.
        penup()
        setpos(xmin, ((a*xmax*xmax)+c))
        pendown()
        pensize(2)
        color("red")

        #to draw every coordinate between the range.
        for y in range(xmin, xmax):
            ysqr = (y*y)
            setpos(y, (a*ysqr)+c)
        done()
    
    #for a parabola with a formula like -ax^2+bx-
    elif c == "":
        c = 0
        b = float(b)
        #to find roots, axis of symetry and y-intercept.
        if b**2-4*a*c >= 0:
            root1 = ((-b - (math.sqrt(b**2-4*a*c)))/2*a)
            root2 = ((-b + (math.sqrt(b**2-4*a*c)))/2*a)
            print("\n\nroots are " + str(root1) + " and " + str(root2))
        else:
            print("\n\nthere is no roots for this parabola")    
        yintercept = c
        print("\ny-intercept is " + str(c) + "\n")   
        print("axis of symetry is x = " + (-b/(2*a)) + "\n")

        #setting the position of the pen to the starting point.
        penup()
        setpos(((-b/(2*a))+xmin), (a*((-b/(2*a))+xmin)**2)+b*((-b/(2*a))+xmin))
        pendown()
        pensize(2)
        color("red")
        #setting the position of the pen to the starting point.
        for y in range((round(-b/(2*a)) + xmin), (round((-b/(2*a))) + xmax)):
            ysqr = (y*y)
            setpos(y, (a*ysqr)+(b*y))
        done()

    #for a parabola with a formula like -ax^2+bx+c-
    else:
        b = float(b)
        c = float(c)

        #to find roots, axis of symetry and y-intercept.
        if b**2-4*a*c >= 0:
            root1 = ((-b - (math.sqrt(b**2-4*a*c)))/2*a)
            root2 = ((-b + (math.sqrt(b**2-4*a*c)))/2*a)
            print("\n\nroots are " + str(root1) + " and " + str(root2))
        else:
            print("\n\nthere is no roots for this parabola")  
        yintercept = str(c)
        print("\ny intercept is " + yintercept + "\n")
        print("axis of symetry is x = " + (-b/(2*a)) + "\n")

        #setting the position of the pen to the starting point.
        penup()
        setpos(((-b/(2*a))+xmin), ((a*((-b/(2*a))+xmin)**2)+b*((-b/(2*a))+xmin)+c))
        pendown()
        pensize(2)
        color("red")

        #setting the position of the pen to the starting point.
        for y in range((round(-b/(2*a)) + xmin), (round((-b/(2*a))) + xmax)):
            ysqr = (y*y)
            setpos(y, ((a*ysqr)+(b*y)+c))
        done()       

Quad()
