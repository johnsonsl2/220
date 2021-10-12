"""
Name: Sara Johnson
Partner: <your partner's name goes here – first and last>

Problem: Write functions that accept arguments and return values, be able to modify an object in a parameter

Certification of Authenticity:
I certify that this assignment is entirely my own work

lab7.py
"""
from math import *

def cash_conversion():
    integer = eval(input("Enter an integer you would like to have the corresponding dollar value of:"))
    output = "{:.2f}".format(integer)
    #the corresponding dollar value of input
    print('$', output)

def encode():
    message = input("Enter the message you would like to encode: ")
    key = eval(input("Enter an integer key value: "))
    for ch in message:
        pre_ord = (ord(ch))
        final_ord = pre_ord + key
        final_ch = (chr(final_ord))
        print(final_ch, end="")

def sphere_area(radius):
    surface_area = (4 * pi) * (radius**2)
    return(surface_area)

def sphere_volume(radius):
    volume = ((4/3) * pi * (radius **3))
    return(volume)

def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return(total)

def sum_n_cubes(n):
    total = 0
    for i in range(1, n + 1):
        cubed = i **3
        total = total + cubed
    return (total)

def encode_better():
    message = input("Enter the message you would like to encode: ")
    key = input("Enter an integer key value: ")
    for i in range(len(message)):
        mess_chr = message[i]
        key_chr = key[i]
        shift = ord(key_chr) - 97
        final_ord = ord(mess_chr) + shift
        final = chr(final_ord)
        print(final, end="")




def main():
    cash_conversion()
    encode()
    sphere_area()
    sphere_volume()
    sum_n()
    sum_n_cubes()
    encode_better()
    pass


main()
