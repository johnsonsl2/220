import math

"""
Name: <Sara Johnson>
<lab2.py>
"""
#Sum of Threes
def sums_of_threes():
    print("Lets find the sum of threes!")
    upper_bound = eval(input('What would you like the upper bound to be? '))
    sum = 0
    for i in range(3,upper_bound +1 ,3):
        sum = i + sum
    print("This is the sum of the threes: ", sum)

#sums_of_threes()
#end of loop

#Multiplication table 10x10

def multiplication_table():
    print("Multiplication Table")
    print( "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    print('1:', end=" ")
    for a in range(1,11,1):
        print( a, end=" ")
    print()
    print('2:', end= " ")
    for b in range(2,21,2):
        print(b, end= " ")
    print()
    print('3:', end=" ")
    for b in range(3, 31, 3):
        print(b, end=" ")
    print()
    print('4:', end=" ")
    for b in range(4, 41, 4):
        print(b, end=" ")
    print()
    print('5:', end=" ")
    for b in range(5, 51, 5):
        print(b, end=" ")
    print()
    print('6:', end=" ")
    for b in range(6, 61, 6):
        print(b, end=" ")
    print()
    print('7:', end=" ")
    for b in range(7, 71, 7):
        print(b, end=" ")
    print()
    print('8:', end=" ")
    for b in range(8, 81, 8):
        print(b, end=" ")
    print()
    print('9:', end=" ")
    for b in range(9, 91, 9):
        print(b, end=" ")
    print()
    print('10:', end=" ")
    for b in range(10, 101, 10):
        print(b, end=" ")
    print()



#end of loop for multitplication

#multiplication_table()

#Computing the area of a triangle

def triangle_area():
    a = eval(input("What is the length of side 'a'?"))
    b = eval(input("What is the length of side 'b'?"))
    c = eval(input("What is the length of side 'c'?"))
    s = (a + b + c)/2
    area_sqrt = s * ((s-a) * (s-b) * (s-c))
    area= math.sqrt(area_sqrt)
    print('The area is', area)


#triangle_area()

#Sum of Squares

def sumSquares():
    print("Lets find the sum of squares")
    lower = eval(input("First, what would you like to be your starting number?"))
    upper = eval(input("Now, what would you like to be your ending number?"))
    sum_sqr = 0
    for i in range(lower, upper + 1, 1):
        sum_sqr = sum_sqr + (i **2)
        #end of loop
    print("This is your sum of squares: ", sum_sqr)

#sumSquares()


#Manually finding the power

def power():
    base = eval(input("Base number: "))
    exponent = eval(input("Exponent number: "))
    answer = 1
    for i in range(exponent):
        answer *= base
    print( base, "^", exponent, "=", answer)
    #end of loop
power()
