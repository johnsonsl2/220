"""
Name: <Sara Johnson>
lab1.py

Problem: This function calculates the area of a rectangle
"""

def calc_area():
    length = 20
    width = 5
    area = length * width
    print("Area =", area)



def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


#User Input: Volume

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)



#Shooting percentage

def calc_shooting_percentage():
    total_shots = eval(input("Enter the number of total shots: "))
    shots_made = eval(input("Enter the number of shots made: "))
    shooting_percentage = (shots_made / total_shots) * 100
    print("Shooting Percentage=", shooting_percentage, "%")




#Coffee shop

def coffee():
    pounds_ordered =eval(input("Enter the number of pounds of coffee ordered: "))
    total_cost = (pounds_ordered * 10.50) + (pounds_ordered * .86) + 1.50
    print("Total Order Cost= $",total_cost)



#Kilometers to miles

def kilometers_to_miles():
    kilometers = eval(input("Enter the number of kilometers traveled: "))
    conversion = kilometers * .621
    print("How many miles traveled =", conversion)

