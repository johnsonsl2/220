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
    outfile = open(out_file_name, "w")

    student_ave = 0
    num_student = 0

    for line in infile.readlines():
        name, num = line.split(': ')
        num_list = num.split(' ')
        new_weight = 0
        average = 0
        for i in range(0, len(num_list), 2):
            weight = int(num_list[i])
            print(weight)
            new_weight = new_weight + weight
        if new_weight < 100:
            outfile.write(name + "'s" + 'average' + ':'  + 'Error: The weights are less than 100.')
        if new_weight > 100:
            outfile.write(name + "'s" + 'average' + ':' + 'Error: The weights are more than 100.')
        else:
            num_students = num_student + 1

            for n in range(0, len(num_list), 2):
                int_num = int(num_list[n])
                grade1 = int(num_list[n + 1])
                weighted_grade = int_num * grade1
                average = weighted_grade / 100

            outfile.write(name + "'s" + ' ' + 'average' + ': ' + str(average) + '\n')















"""


    for line in infile:

        num = []
        line_list = line.split(' ')
        for n in line_list():
            try:
                l.append(float(num))
            except ValueError:
                pass

        #name_str = str(name)
        #outfile.write(name_str)
        #print(nums)
        new_weight = 0
        for i in range(0, len(num), 2):
            weight = num[i]
            new_weight = new_weight + weight
        if new_weight <= 100:
            outfile.write(name + ':' + 'Error: The weights are less than 100.')
        if new_weight < 100:
            outfile.write(name + ':'+ 'Error: The weights are more than 100.')
        else:
            set_list = [nums[x:x + 2] for x in range(0, len(nums), 2)]







    #print(data)




    #print(outdata)
"""



weighted_average('grades.txt', 'avg.txt')
