#EIA, twwsts, 3 April 2018.
#This a program for to draw quadratic functions. It also gives the roots of the parabola.

from turtle import *
import math

print("ax^2 + bx + c\n\njust click enter if there is not one")
print("the parabola might not be seen if the axis of symetry is too much far away to origin.")
print("`b` value necessary for program to work properly.\n\n")

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

    #assigning values.
    values = {"a": 0, "b": 0, "c": 0}
    for value in values:
        multiplier = input(value + " = ")
        while type(multiplier) is str:
            if multiplier == "":
                multiplier = 0
            else:
                try:
                    multiplier = float(multiplier)
                except ValueError:
                    print("This value is not valid. It possibly contains letters or special characters. Only numbers or decimals please.")
                    multiplier = input(value + " = ")
                values[value] = multiplier
    a = values.get("a")
    b = values.get("b")
    c = values.get("c")
    aos = 0                 #axis of symetry is set to 0.

    #to open the turtle window.
    turtleSettings()

    if True:

        """
        #to find roots, axis of symetry and y-intercept.
        if b**2-4*a*c >= 0 and a >= 1:
            root1 = ((-b - (math.sqrt(b**2-4*a*c)))/2*a)
            root2 = ((-b + (math.sqrt(b**2-4*a*c)))/2*a)
            print("\n\nroots are " + str(root1) + " and " + str(root2))
        else:
            print("\n\nthere is no roots for this parabola")
        """
        yintercept = str(c)
        print("\ny intercept is " + yintercept + "\n")

        #finding the axis of symetry if a is not 0.
        if a != 0:
            aos = (-b / (2 * a))
            axisOfSymetry = ("axis of symetry is x = " + str(aos) + "\n")
            print(axisOfSymetry)

        #setting the position of the pen to the starting point.
        penup()
        setpos(((aos)+xmin), ((a*((aos)+xmin)**2)+b*((aos)+xmin)+c))
        pendown()
        pensize(2)
        color("red")

        #setting the position of the pen to the starting point.
        for x in range((round(aos) + xmin), (round(aos) + xmax)):
            xsqr = (x*x)
            setpos(x, ((a*xsqr)+(b*x)+c))
        done()

Quad()