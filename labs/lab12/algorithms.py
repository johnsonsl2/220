"""
Name: Sara Johnson
algorithms.py

Problem: Read in a file of numbers and return and find in a list

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

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
    for x in range(len(value)):
        if value[x] == search_val:
            return True


def is_in_binary(search_val, values):
    low = 0
    high = len(values) - 1
    while low <= high :
        middle = (low + high) // 2
        middle_value = values[middle]
        if search_val == middle_value:
            return middle
        if search_val < middle_value:
            high = middle - 1
        if search_val > middle_value:
            low = middle + 1
    return False

def selection_sort(values):
    start = 0
    while not start == len(values) - 1:
        min = start
        for i in range(start, len(values)):
            if values[i] < values[min]:
                min = i
        move_num = values[start]
        values[min] = values[start]
        values[min] = move_num
        start = start + 1
    print(values)

def main():
    is_in_linear()
    is_in_binary()
    selection_sort()


    pass