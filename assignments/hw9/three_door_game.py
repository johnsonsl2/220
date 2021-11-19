"""
Name: Sara Johnson
mean.py

Problem: Code a graphic where two balls bounce of each other

Certification of Authenticity:
I certify that this assignment is entirely my own work

"""

from graphics import *
from button import *
from random import randint

def main():

    win = GraphWin("Three Door Game", 750, 600)
    header = Text(Point(375,50), "Guess the secret door")
    header.setSize(18)
    header.draw(win)

    footer = Text(Point(375, 550), "click to choose the secret door")
    footer.setSize(15)
    footer.draw(win)

    door1 = Button(25, 100, 225, 500, "Door 1")
    door2 = Button(272, 100, 475, 500, "Door 2")
    door3 = Button(525, 100, 725, 500, "Door 3")

    door1.draw(win)
    door2.draw(win)
    door3.draw(win)


    pick = randint(1, 3)

    if pick == 1:
        pick = 'door1'
    if pick == 2:
        pick = 'door2'
    if pick == 3:
        pick = 'door3'

    point = win.getMouse()

    header.undraw()
    footer.undraw()

    win_header = Text(Point(375,50), "You guessed the right door! You win!!!")
    loser_header = Text(Point(375,50), "You guessed the wrong door! You lose!!!")

    loser_footer_statement = ("My secrete door is {}".format(pick))
    loser_footer = Text(Point(375, 550), loser_footer_statement)
    finish_footer = Text(Point(375, 550), "Click to close")

    def picked_door(pick):
        pick.color_button("green")
        pick.draw(win)


    if door1.is_clicked(point) == True:
        if pick == 'door1':
            picked_door(door1)
            win_header.draw(win)
            win.getMouse()
            finish_footer.draw(win)

        elif pick != 'door1':
            door1.color_button("Red")
            loser_footer.draw(win)
            win.getMouse()
            loser_footer.undraw()
            finish_footer.draw(win)


    elif door2.is_clicked(point) == True:
        if pick == 'door2':
            picked_door(door2)
            win_header.draw(win)
            win.getMouse()
            finish_footer.draw(win)

        if pick != 'door2':
            door1.color_button("Red")
            loser_footer.draw(win)
            win.getMouse()
            loser_footer.undraw()
            finish_footer.draw(win)


    if door3.is_clicked(point) == True:
        if pick == 'door3':
            picked_door(door3)
            win_header.draw(win)
            win.getMouse()
            finish_footer.draw(win)

        if pick != 'door3':
            door3.color_button("Red")
            loser_footer.draw(win)
            win.getMouse()
            loser_footer.undraw()
            finish_footer.draw(win)


    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
