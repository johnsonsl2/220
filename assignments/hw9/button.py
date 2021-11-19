"""
Name: Sara Johnson
button.py

Problem: Create class for the buttons that will eventually be applied to the game

Certification of Authenticity:
I certify that this assignment is entirely my own work

"""



from graphics import *
class Button:

    def __init__(self, top_corner_x, top_corner_y, bottom_corner_x, bottom_corner_y, label):
        #shape should be a rectangle object based off corner coordinates
        #label should be string

        self.shape = Rectangle(Point(top_corner_x, top_corner_y), Point(bottom_corner_x, bottom_corner_y))

        center = self.shape.getCenter()
        self.label = str(label)
        self.win = GraphWin()
        self.color = ""
        self.point = Point
        self.message = Text(center, self.label)

    def get_label(self):
        return str(self.label)

    def color_button(self, color):
         self.shape.setFill(color)

    def draw(self, win):
        self.shape.draw(win)
        self.message.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.message.undraw()


    def is_clicked(self, point):
        if point ==











