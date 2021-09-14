"""
Name: <Sara Johnson>
<lab3>.py

Problem: Develop simple program using for loops, inputs, outputs and arithmetic

Certification of Authenticity:
I certify that this assignment is entirely my own work

"""


#Finding an average

def average():
    print("Lets find the average of your homework grades!")
    num_grades = eval(input("How many grades do you have?"))
    sum = 0
    for i in range(1, num_grades + 1):
        statement = "What is your average for HW" + str(i)
        HWave = eval(input(statement))
        sum= sum + HWave
        average = sum / num_grades
    print("This is your homework average:", average)


#average()


#Donation Jar

def tip_jar():
    print("Lets find the amount of money in the tip jar!")
    sum = 0
    for i in range (1, 6):
        prompt = "How much money are you tipping Person" + str(i) + "?"
        tip = eval(input(prompt))
        sum = sum + tip
    print("There is $",sum, "in the tip jar")
#tip_jar()

#Computing the square root

def newton():
    print("Lets approximate the square root using Sir Isaac Newton's method!")
    x = eval(input("What number would you like approximate it's square root?"))
    approx = eval(input("How many times would you like to improve the approximation"))
    for i in range(2, approx + 1):
        approx = ((i + (x / i))/(2))
    print("This is the approximation of", x, ":", approx)
#newton()

#Output a sequence

def sequence():
    print("You want to see a pattern? Me too!")
    end = eval(input("How many numbers of terms do you want in the series?"))
    pattern = 1
    for i in range(end):
        pattern = pattern + (i % 2) * 2
        print(pattern, end= " ")


#sequence()

def pi():
    print("You want to see a pattern for pi? Me too!")
    n = eval(input("How many numbers of terms do you want in the series?"))
    bottom = 1
    top =
    for i in range(n):
        top = top + (i % 2) * 2
    print(pattern1)
    for b in range(n):
        bottom = bottom + (b % 2) * 2
    print(pattern0)
pi()


