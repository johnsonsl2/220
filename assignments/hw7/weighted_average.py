"""
Name: Sara Johnson
mean.py

Problem: Find the weighted and average grades from a text file

Certification of Authenticity:
I certify that this assignment is entirely my own work

"""


def weighted_average(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    class_ave = 0
    students = 0
    for line in infile.readlines():
        name, num = line.split(': ')
        num_list = num.split(' ')
        new_weight = 0
        wga = 0
        for i in range(0, len(num_list), 2):
            weight = int(num_list[i])
            new_weight = new_weight + weight
        if new_weight < 100:
            outfile.write(name + "'s " + 'average' + ':'  + ' Error: The weights are less than 100.' + '\n')
        elif new_weight > 100:
            outfile.write(name + "'s " + 'average' + ':' + ' Error: The weights are more than 100.'+ '\n')
        else:
            students = students + 1
            for n in range(0, len(num_list), 2):
                int_num = int(num_list[n])
                grade1 = int(num_list[n + 1])
                weighted_grade = int_num * grade1
                wga = wga + weighted_grade
            average = round( wga / 100 , 1)
            outfile.write(name + "'s" + ' ' + 'average' + ': ' + str(average) + '\n')
            class_ave = class_ave + average
    total_class_ave = round( class_ave / students, 1)
    outfile.write('Class average: ' + str(total_class_ave))

def main():
    weighted_average('grades.txt', 'avg.txt')

if __name__ == '__main__':
    main()
