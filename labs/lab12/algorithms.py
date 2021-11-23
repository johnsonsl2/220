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
    if value.count(str(search_val)) > 0:
        return True
    elif value.count(str(search_val)) == 0:
        return False




def main():
    #is_in_linear()
    pass