"""
Name: Sara Johnson
lab4.py

Problem: Develop simple program using graphics package and practice accumulating sequences

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

from graphics import *
from math import *


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """

    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
        #moditifying this to squares
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to add square")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(50,50), Point(70,70) )
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)


    # allows the user to click multiple times to clone square
    for i in range(num_clicks):
        p = win.getMouse()
        #c = shape.getMouse()  # center of c

     # move amount is distance from center of circle to the
     # point where the user clicked
        dx = p.getX() #- c.getX()
        dy = p.getY() #- c.getY()
        shape = Rectangle(Point(dx - 10, dy - 10), Point(dx + 10, dy + 10))
        shape.setFill("red")
        shape.setOutline("red")
        shape.draw(win)

    inst_pt1 = Point(width / 2, 10)
    instructions = Text(inst_pt1, "Click again to quit")
    instructions.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """

    width = 500
    height = 500
    win1 = GraphWin("Build a Rectangle", width, height)


    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to draw a rectangle")
    instructions.draw(win1)

    pointA = win1.getMouse()
    pointB = win1.getMouse()
    rec = Rectangle(pointA, pointB)
    rec.setFill("red")
    rec.setOutline("black")
    rec.draw(win1)

    dimenAx = pointA.getX()
    dimenAy = pointA.getY()
    dimenBx = pointB.getX()
    dimenBy = pointB.getX()
    reclength = abs(dimenBx - dimenAx)
    recheight = abs(dimenBy - dimenAy)
    perimeter = (2 * recheight) + (2*reclength)
    area = (reclength * recheight)

    inst_pt = Point(width / 2, 10 )
    areatext = "Rectangle Area:", area
    answer = Text(inst_pt, areatext)
    answer.draw(win1)

    inst_pt = Point(width / 2, 30)
    perimetertext = "Rectangle Perimeter:", perimeter
    answer1 = Text(inst_pt, perimetertext )
    answer1.draw(win1)



    inst_pt1 = Point(width / 2, height / 2)
    instructions = Text(inst_pt1, "Click again to quit")
    instructions.draw(win1)
    win1.getMouse()
    win1.close()

#rectangle()


def circle():
    # Creates a graphical window
    width = 400
    height = 400
    win2 = GraphWin("Draw a Circle", width, height)

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click Twice to draw a circle")
    instructions.draw(win2)

    pointA = win2.getMouse()
    pointB = win2.getMouse()

    dimenAx = pointA.getX()
    dimenAy = pointA.getY()
    dimenBx = pointB.getX()
    dimenBy = pointB.getX()
    x = (dimenAx - dimenBx) * (dimenAx - dimenBx)
    y = (dimenAy - dimenBy) * (dimenAy - dimenBy)
    radius = sqrt(x + y)


    cir = Circle(pointA, radius)
    cir.setFill("red")
    cir.setOutline("black")
    cir.draw(win2)



    inst_pt = Point(width / 2, 30)
    radiustext = "Circle Radius:", radius
    answer1 = Text(inst_pt, radiustext)
    answer1.draw(win2)



    inst_pt1 = Point(width / 2, height / 2)
    instructions = Text(inst_pt1, "Click again to quit")
    instructions.draw(win2)
    win2.getMouse()
    win2.close()




def main():
    #squares()
    # rectangle()
    #circle()
    # pi2()


main()
