"""
Name: Sara Johnson
lab8.py

Problem:Inputing files and coding out files to demonstrate work for the instructor

Certification of Authenticity:
I certify that this assignment is entirely my own work

"""
from encryption import encode

def numbers_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    for line in infile.readlines():
        words = line.split(" ")
        word_count = len(words)
        num_order = 0
        for i in range(word_count):
            words_ind = words[i]
            num_order = num_order + 1
            num_order_str = str(num_order)
            line_statement = (num_order_str + " " + words_ind)
            #print_statement =
            outfile.write(line_statement + '\n')
    infile.close()
    outfile.close()



def hourly_wage(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    for line in infile.readlines():
        word = line.split(" ")
        first_name = word[0]
        last_name = word[1]
        current_wage = word[2]
        cwf = float(current_wage)
        hours_worked = word[3]
        hwf = float(hours_worked)
        new_hourly = hwf + 1.65
        week_pay = new_hourly * hwf
        week_pay_str = str(week_pay)
        outfile.write(first_name + " " + last_name + " " + "$" + week_pay_str +'\n')
    infile.close()
    outfile.close()


def calc_check_sum(isbn):
    final = 0
    for i in range(len(isbn)):
        num = isbn[i]
        num_int = int(num)
        mult = len(isbn) - i
        pre = num_int * mult
        final = final + pre
    print(final)



def send_message(file, friend):
    infile = open(file, "r")
    file_name = str(friend + ".txt")
    outfile = open(file_name, "w")
    for line in infile:
        outfile.write(line)
    infile.close()
    outfile.close()



def send_safe_message(file, friend, key):
    infile = open(file, "r")
    file_name = str(friend + ".txt")
    outfile = open(file_name, "w")
    message = infile.read()
    new_message = encode(message,key)
    outfile.write(new_message)
    infile.close()
    outfile.close()








def main():
    #numbers_words()
    #hourly_wage()
    #calc_check_sum()
    #send_message()
    #encode()
    #send_safe_message()


    pass


main()
