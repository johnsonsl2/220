"""
Name: Sara Johnson
mean.py

Problem: Code a graphic where two balls bounce of each other

Certification of Authenticity:
I certify that this assignment is entirely my own work

"""

from graphics import *
from button import *

win = GraphWin("Three Door Game", 400, 500)
button1shape = ([1, 2], [4, 6])

button1 = Button(10, 10, 100, 100, "Please")

button1.draw(win)

button1.draw(win)



win.getMouse()
win.close()

button1.undraw()
