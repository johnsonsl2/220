"""
Name: Sara Johnson
lab13.py

Problem: Use while loops and list

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""
def is_in_binary(search_val, values):
    low = 0
    high = len(values) - 1
    while low <= high :
        middle = (low + high) // 2
        middle_value = values[middle]
        if search_val == middle_value:
            return middle
        if search_val < middle_value:
            right = middle - 1
        if search_val > middle_value:
            left = middle + 1
    return False

def star_find(filename):
    infile = open(filename, "r")
    for line in infile.readlines():
        num_list = line.split(" ")
        occ = []
    while len(occ) < 5:
        for x in range(len(num_list)):
            intn = int(num_list[x])
            if intn >= 4000 and intn <= 5000:
                occ.append(intn)
    print("Five pulses were found:")
    print(occ[0])
    print(occ[1])
    print(occ[2])
    print(occ[3])
    print(occ[4])
    ind = num_list.index(str(occ[4]))
    print("It took", ind, "searches to before finding the fifth signal")


def main():
    is_in_binary()
    star_find("signals.txt")
    pass


main()
