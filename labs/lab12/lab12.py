"""
Name: Sara Johnson
lab12.py

Problem: Use while loops and list

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

import algorithms

def find_and_remove(list, value):
    pos = list.index(value)
    list.insert(pos, "Sara")
    list.remove(value)
    print(list)

def good_input():
    user_input = eval(input("Enter a number between 1 and 10:"))
    if (1 <= user_input <= 10):
        print("good input")
        return True
    else:
        while not user_input == (1 >= user_input <= 10):
            user_input = eval(input("Enter a number between 1 and 10:"))
            if (1 <= user_input <= 10):
                print("good input")
                return True


def num_digits():
    user_input = eval(input("Enter a positive number:"))
    while user_input > 0:
        x = 1
        if (user_input >=1) and (user_input < 10):
            print("The number of digits: ", x)
            user_input = eval(input("Enter a positive number:"))

        else:
            tens = user_input // 10
            while tens > 0:
                x = x + 1
                tens = tens // 10
                print("The number of digits: ", x)
            user_input = eval(input("Enter a positive number:"))






def main():
    #list = [1,2,2,5,4]
    #find_and_remove(list,5)
    #good_input()
    num_digits()
    pass


main()

#Algorithms.py

def read_data(filename):
    #enter a files name
    infile = open(filename, "r")
    line = infile.readlines()
    i = 0

    num_list =[]
    while i < len(line):
        num = line[i]
        num = num.strip('\n')
        num_list.append(num)
        if num.count(" ") > 0:
            x = 0
            num1 = num.split(" ")
            while x < len(num1):
                n = num1[x]
                num_list.append(n)
                x +=1
        i +=1
    return num_list

def is_in_linear(search_val, value):
    #search_val is the value you want to find, value is a list of values
    if value.count(str(search_val)) > 0:
        return True
    elif value.count(str(search_val)) == 0:
        return False




def main():
    #is_in_linear()
    pass