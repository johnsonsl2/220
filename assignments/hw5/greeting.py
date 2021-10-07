"""
Name: Sara Johnson
mean.py

Problem: Write a program that creates a Valentine's Day card

Certification of Authenticity:
I certify that this assignment is entirely my own work

"""

from graphics import *

def main():
    win = GraphWin("Valentine's Day Card", 400, 500)
    win.setBackground("Pink")

    center_point_a = Point(150, 150)
    center_point_b = Point(250, 150)

    circle_a = Circle(center_point_a, 52)
    circle_b = Circle(center_point_b, 52)

    circle_a.setFill("Red")
    circle_b.setFill("Red")
    circle_a.setOutline("Red")
    circle_b.setOutline("Red")

    circle_a.draw(win)
    circle_b.draw(win)

    center_point_tri = Point(200, 350)

    #point_tri_a = win.getMouse()
    #print(point_tri_a)

    point_tri_a = Point(103.0, 173.0)
    point_tri_b = Point(298, 173.0)

    triangle = Polygon(center_point_tri, point_tri_a, point_tri_b)
    triangle.setFill("Red")
    triangle.setOutline("Red")
    triangle.draw(win)

    #pointA = win.getMouse()
    #print(pointA)
    #pointB = win.getMouse()
    #print(pointB)
    #pointC = win.getMouse()
    #print(pointC)
    #pointD = win.getMouse()
    #print(pointD)


    center_rec = Polygon(Point(193.0, 155.0), Point(209.0, 154.0), Point(209.0, 174.0), Point(190.0, 173.0))
    center_rec.setFill("Red")
    center_rec.setOutline("Red")
    center_rec.draw(win)



    text_point = Point(200, 400)
    message = Text(text_point, "Happy Valentine's Day!")
    message.setSize(20)
    message.setStyle("bold italic")
    message.draw(win)

    time.sleep(1.5)

    #arrow
    start_point_line_b = Point(389.0, 10.0)
    start_point_line_a = Point(300, 100)
    arrow_line = Line(start_point_line_a, start_point_line_b)
    arrow_line.draw(win)


    start_point_tri_a = Point(300.0, 88.0)
    #print(start_point_tri_a)
    start_point_tri_b = Point(300, 100)
    start_point_tri_c = Point(312, 100)

    arrow_tri = Polygon(start_point_tri_a, start_point_tri_b, start_point_tri_c)
    arrow_tri.setFill("Black")
    arrow_tri.setOutline("Black")
    arrow_tri.draw(win)


    slope_point_ata = Point(389.0, 10.0)
    slope_point_atb = Point(383.0, 16.0)

    end_point_ataa = Point(389.0,2)
    end_point_atab = Point(397.0, 10)
    arrow_tail_aa = Line(slope_point_ata,end_point_ataa )
    arrow_tail_ab = Line(slope_point_ata, end_point_atab)
    arrow_tail_aa.draw(win)
    arrow_tail_ab.draw(win)

    end_point_atba = Point(377.0, 8)
    end_point_atbb = Point(389.0, 16)
    arrow_tail_ba = Line(slope_point_atb, end_point_ataa)
    arrow_tail_bb = Line(slope_point_atb, end_point_atab)
    arrow_tail_ba.draw(win)
    arrow_tail_bb.draw(win)


    for i in range(0,40):
        arrow_line.move(-11.125, 11.25)
        #arrow_line.draw(win)
        arrow_tri.move(-11.125, 11.25)
        #arrow_tri.draw(win)
        arrow_tail_aa.move(-11.125, 11.25)
        #arrow_tail_aa.draw(win)
        arrow_tail_ab.move(-11.125, 11.25)
        #arrow_tail_ab.draw(win)
        arrow_tail_ba.move(-11.125, 11.25)
        #arrow_tail_ba.draw(win)
        arrow_tail_bb.move(-11.125, 11.25)
        #arrow_tail_bb.draw(win)
        time.sleep(.1)

    msg_end = "Click again to close window"
    inst2 = Text(Point(200,450), msg_end)
    inst2.draw(win)

    win.getMouse()
    win.close()



if __name__ == '__main__':
    main()