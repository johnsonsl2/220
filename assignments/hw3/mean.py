"""
Name: <Sara Johnson>
<mean.py>

Problem: Calculate the mean using input, arithmetic and providing outputs

Certification of Authenticity:
I certify that this assignment is entirely my own work

"""

from math import *


def main():
    print("Lets find the RMS Average, the Harmonic Mean and the Geometric Mean")
    numofnum = eval(input("How many values do you have?"))
    print("Please enter your values")
    sum = 0
    sum1 = 0
    sum2 = 0
    sum3 = 1
    for i in range(1, numofnum + 1):
        statement = "Enter Value " + str(i) + ":"
        Numave = eval(input(statement))
        sum = sum + Numave
        arithmetic_mean = sum / numofnum
        #print(arithmetic_mean)
        #rms
        sum1 = sum1 + (Numave ** 2)
        rms = sqrt( sum1 / numofnum )
        rms_f = round(rms,3)
        #harmonic mean
        sum2 = sum2 + (1/ Numave)
        hm = numofnum / sum2
        harmonic_mean = round(hm, 3)
        #geometric mean
        #for c in range(1, numofnum):
        sum3 = sum3 * Numave
        gm = (sum3) ** (1/numofnum)
        geometric_mean = round(gm, 3)
    print("RMS Average: ", rms_f)
    print("Harmonic Mean: ", harmonic_mean)
    print("Geometric Mean: ", geometric_mean)






if __name__ == '__main__':
    main()

