"""
Name: Sara Johnson
mean.py

Problem: Find the weighted and average grades from a text file

Certification of Authenticity:
I certify that this assignment is entirely my own work

"""
# text format firstName lastName: w1 g1 w2 g2 ... wn gn

def weighted_average(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    data = infile.read()
    outfile = open(out_file_name, "w+")

    for line in data:
        name, nums = line.split(":")
        #print(nums)
        new_weight = 0
        for i in range(0, len(nums), 2):
            weight = nums[i]
            new_weight = new_weight + weight
        if new_weight > 100:
            print("Error: The weights are more than 100.")
        elif new_weight < 100:
            print('Error: The weights are less than 100.')
        elif:
            set_list = [nums[x:x + 2] for x in range(0, len(nums), 2)]






    print(data)




    #print(outdata)



#main()