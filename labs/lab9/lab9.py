"""
Name: Sara Johnson
lab9.py

Problem: Modifying lists and demonstrating work for the instructor

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


def addTens(nums):
    for i in range(len(nums)):
        nn = int(nums[i]) + 10
        nums.remove(nums[i])
        nums.insert(i, nn)

def squareEach(nums):
    for i in range(len(nums)):
        nn = float(nums[i])
        nn2 = nn * nn
        print(nn2)
        nums.remove(nums[i])
        nums.insert(i, nn2)
    print(nums)



def sumList(nums):
    nn = 0
    for i in range(len(nums)):
        nn = nums[i] + nn
    return(nn)


def toNumbers(strList):
    nn = 0
    for i in range(len(strList)):
        nn = float(strList[i]) + nn
    print(nn)


def writeSumOfSquares():
    in_file_name = input('Enter the name of the input file: ')
    infile = open(in_file_name, "r")
    outfile = open('sum_out.txt', "w")
    for line in infile.readlines():
        num = line.split(" ")
        num_count = len(num)
        num_order = 0
        nn = 0
        sumnum = 0
        for i in range(len(num)):
            nn = float(num[i])
            nn2 = nn * nn
            sumnum = nn2 + sumnum
        sum_statement = ("Sum of Squares = " + str(sumnum))
        outfile.write(sum_statement +'\n')
    infile.close()
    outfile.close()



def starter():
    weight = eval(input("Enter weight: "))
    numsWins = eval(input("Enter the number of matches wins: "))
    if ((weight > 150) and (weight < 160) and (numsWins >= 5)) or ((weight > 199) or (numsWins > 20)):
        print("This individual should start.")
    elif not ((weight > 150) and (weight < 160) and (numsWins >= 5)) or ((weight > 199) or (numsWins > 20)):
        print("This individual should not start.")

def leapYear(year):
    if not year % 400:
        return True
    elif year % 400:
        return False

from graphics import *
from math import *

def circleOverlap():
    width = 500
    height = 500
    win2 = GraphWin("Draw a Circle", width, height)

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click Twice to draw a circle")
    instructions.draw(win2)

    centerA = win2.getMouse()
    pointB = win2.getMouse()

    cdimenAx = centerA.getX()
    cdimenAy = centerA.getY()
    dimenBx = pointB.getX()
    dimenBy = pointB.getY()
    x = (cdimenAx - dimenBx) * (cdimenAx - dimenBx)
    y = (cdimenAy - dimenBy) * (cdimenAy - dimenBy)
    radiusA = sqrt(x + y)

    cir = Circle(centerA, radiusA)
    cir.setFill("red")
    cir.setOutline("black")
    cir.draw(win2)

    dimenCir2x = 100
    dimenCir2y = 100
    centerB = 100, 100
    radiusB = 40
    cir2 = Circle(centerB, 40)
    cir2.setFill('black')
    cir2.draw(win2)

    distx = (cdimenAx - dimenCir2x) * (cdimenAx - dimenCir2x)
    disty = (cdimenAy - dimenCir2y) * (cdimenAy - dimenCir2y)

    distance = sqrt(distx + disty)
    radius_diff = radiusA - radiusB
    if distance > radius_diff and radius_diff > 0:
        inst_ptB = Point(width / 2, height - 30)
        finalA = Text(inst_ptB, "The circles do not overlap")
        finalA.draw(win2)
    elif distance < radius_diff or radius_diff < 0:
        inst_ptB = Point(width / 2, height - 30)
        finalB = Text(inst_ptB, "The circles do overlap")
        finalB.draw(win2)

    win2.getMouse()
    win2.close()



def main():
    #addTens()
    #squareEach()
    #sumList()
    #toNumbers()
    #writeSumOfSquares()
    #starter()
    #leapYear()
    #circleOverlap()


    pass


main()
