"""
Name: <Sara Johnson>
lab5.py
"""

from graphics import *
from math import *

from graphics import Text

"""
def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()
"""

def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.

    pointA = win.getMouse()
    pointB = win.getMouse()
    pointC = win.getMouse()
    tri = Polygon(pointA, pointB, pointC)
    tri.setFill("red")
    tri.setOutline("black")
    tri.draw(win)

    dimenAx = pointA.getX()
    dimenAy = pointA.getY()
    dimenBx = pointB.getX()
    dimenBy = pointB.getX()
    dimenCx = pointC.getX()
    dimenCy = pointC.getY()

    abdx = (dimenBx - dimenAx)
    abdy = (dimenBy - dimenAy)
    ablen = sqrt((abdx ** 2) + (abdy ** 2))

    bcdx = (dimenCx - dimenBx)
    bcdy = (dimenCy - dimenBy)
    bclen = sqrt((bcdx ** 2) + (bcdy ** 2))

    cadx = (dimenAx - dimenCx)
    cady = (dimenAy - dimenCy)
    calen = sqrt((cadx ** 2) + (cady ** 2))

    perimeter = ablen + bclen + calen
    s = (ablen + bclen + calen) / 2
    area = sqrt(s * (s - ablen) * (s - bclen) * (s - calen))

    # and display its area in the graphics window.

    inst_pt = Point(win_width / 2, 10)
    areatext = "Triangle Area:", area
    answer = Text(inst_pt, areatext)
    answer.draw(win)

    inst_pt = Point(win_width / 2, 30)
    perimetertext = "Triangle Perimeter:", perimeter
    answer1 = Text(inst_pt, perimetertext)
    answer1.draw(win)
    # Wait for another click to exit
    win.getMouse()
    win.close()

    # and display its area in the graphics window.


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win1_width = 400
    win1_height = 400
    win1 = GraphWin("Color Shape", win1_width, win1_height)
    win1.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    insta_width = win1_width / 2
    insta_height = (win1_height - 20)
    inst = Text(Point(insta_width, insta_height), msg)
    inst.draw(win1)

    # the text that starts in entry box

    # create circle in window's center
    shape = Circle(Point(win1_width / 2, win1_height / 2 - 30), 50)
    shape.draw(win1)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win1_width / 2 - 50, win1_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    input_red = Entry(Point(win1_width / 2 , win1_height / 2 + 40), 5)
    input_red.draw(win1)
    input_red.setText("0")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    input_green = Entry(Point(win1_width / 2, win1_height / 2 + 70 ), 5)
    input_green.draw(win1)
    input_green.setText("0")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    input_blue = Entry(Point(win1_width / 2, win1_height / 2 + 100), 5)
    input_blue.draw(win1)
    input_blue.setText("0")


    # display rgb text
    red_text.draw(win1)
    green_text.draw(win1)
    blue_text.draw(win1)

    for i in range(5):
        win1.getMouse()
        input_red_get = eval(input_red.getText())
        input_green_get = eval(input_green.getText())
        input_blue_get = eval(input_blue.getText())
        color = color_rgb(input_red_get, input_green_get, input_blue_get)
        shape.setFill(color)
        #shape.clone(win1)

    # create text instructions
    inst.undraw()

    msg_end = "Click again to close window"
    inst2 = Text(Point(insta_width, insta_height), msg_end)
    inst2.draw(win1)

    # Wait for another click to exit
    win1.getMouse()
    win1.close()


def process_string():
    string = input(str("Write a word or phrase: "))
    q1 = string[0]
    print("1. The first character in the string: ", q1)
    q2 = string[-1]
    print("2. The last character in the sting: ", q2)
    q3 = string[2:6]
    print("3. The characters inclusively in positions 2 - 5 of the string: ", q3)
    q4 = string[0:]
    print("4. The concatenation of the first and last character of the string: ", q4)
    q5a = string[0:3]
    q5 = q5a * 10
    print("5. The first three characters in the string repeated 10 times: ", q5)
    print("6. Each character in the string printed one character per line")
    for letter in string:
        print(letter)
    q7 = len(string)
    print("The number of characters in the string: ", q7)


def process_list():
    pt = Point(5, 10)
    values = [5,"hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x =  values[0] + values[2]
    print(x)
    x = values[1] * values[0]
    print(x)
    x = list[values[2], values[3], values[4]]
    print(x)
    x = list[values[2], values[3], values[0]]
    print(x)
    new = float(values[5])
    x = list[values[2], values[0], new]
    print(x)
    x = values[2] + values[0] + new
    print(x)
    x = len(values)
    print(x)



def another_series():
    num_terms = eval(input("How many terms do you want? "))
    series = [2, 4, 6]
    left_over_three = num_terms %3
    mult_by_three = num_terms - left_over_three
    times_of_string = mult_by_three / 3
    patterna = series[0:2] * times_of_string
    print(patterna)

another_series()

#def main():
    #target()
    #triangle()
    #color_shape()
    #pass
    #process_string()
    #process_list()


#main()
