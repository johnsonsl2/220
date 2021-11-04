"""
Name: Sara Johnson
mean.py

Problem: Code a graphic where two balls bounce of each other

Certification of Authenticity:
I certify that this assignment is entirely my own work

"""

from graphics import *
from math import *
from random import randint


def get_random_color():
    cr = color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    return cr


def get_random(move_amount):
    num1 = int(move_amount) * -1
    nma = randint(num1, move_amount)
    return nma


def did_collide(circ1, circ2):
    dimen_Circ1x = circ1.getCenter().getX()
    dimen_Circ1y = circ1.getCenter().getY()
    dimen_Circ2x = circ2.getCenter().getX()
    dimen_Circ2y = circ2.getCenter().getY()

    distx = (dimen_Circ2x - dimen_Circ1x) ** 2
    disty = (dimen_Circ2y - dimen_Circ1y) ** 2

    distance = sqrt(distx + disty)

    if distance <= 80:
        return True



def hit_vertical(ball):
    if (0 < ball.getCenter().getY() <= 40) or (ball.getCenter().getY() >= 460):
        return True


def hit_horizontal(ball):
    if (0 < ball.getCenter().getX() <= 40) or (ball.getCenter().getX() >= 460):
        return True

def main():
    width = 500
    height = 500
    win = GraphWin("Bumper Test", width, height)

    radius = 40
    center1 = Point(randint(40, 250), randint(40, 460))
    center2 = Point(randint(240, 460), randint(40, 460))

    circ1 = Circle(center1, radius)
    circ2 = Circle(center2, radius)

    color1 = get_random_color()
    color2 = get_random_color()
    circ1.setFill(color1)
    circ1.setOutline(color1)
    circ2.setFill(color2)
    circ2.setOutline(color2)

    circ1.draw(win)
    circ2.draw(win)

    circ2.getCenter().getX()

    mb1a = get_random(5)
    mb1b = get_random(5)
    mb2a = get_random(5)
    mb2b = get_random(5)

    while True:
        circ1.move(mb1a, mb1b)
        circ2.move(mb2a, mb2b)

        if hit_vertical(circ1):
            mb1b = mb1b * -1
            circ1.move(mb1a, mb1b)

        elif hit_vertical(circ2):
            mb2b = mb2b * -1
            circ2.move(mb2a, mb2b)

        elif hit_horizontal(circ1):
            mb1a = mb1a * -1
            circ1.move(mb1a, mb1b)

        elif hit_horizontal(circ2):
            mb2a = mb2a * -1
            circ2.move(mb2a, mb2b)

        elif did_collide(circ1, circ2):
            mb1a = mb1a * -1
            mb1b = mb1b * -1
            mb2a = mb2a * -1
            mb2b = mb2b * -1
            circ1.move(mb1a, mb1b)
            circ2.move(mb2a, mb2b)

        time.sleep(.01)


if __name__ == '__main__':
    main()
