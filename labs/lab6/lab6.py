"""
Name: Sara Johnson
lab6.py

Problem: Demonstrate using strings and lists

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input('Enter your first and last name: ')
    name_list = name.split()
    first_name = name_list[0]
    last_name = name_list[1]
    print(last_name,",", first_name)


def company_name():
    """
    enter internet domain and display company name only
    """
    domain = input('Enter a three-part internet domain: ')
    domain_list = domain.split('.')
    company = domain_list[1]
    print(company)

def initials():
    """
    Get initials from students
    """
    num_students = eval(input("Enter the number of student's names are there: "))
    for i in range(1, num_students + 1):
        statement1 = "Enter the first name of student " + str(i) + ": "
        first_name = input(statement1)
        statement2 = "Enter the last name of student " + str(i) + ": "
        last_name = input(statement2)
        first_initial = first_name[0]
        last_initial = last_name[0]
        initial_final = first_initial.upper() + last_initial.upper()

        print(first_name, "'s initials are ", initial_final)


def names():
    #num_names = eval(input("Enter numbers of names: "))
    all_names = input("Enter people's names, seperated by commas: ")
    l1 = all_names.split(',')
    #loopnum = (num_names * 2) +1
    print("The initials are ", end=" ")
    #combo = " "
    for i in range( (len(l1)) + 1 ):
        name = l1[i]
        names = name.split(' ')
        first_name = names[0]
        last_name = names[1]
        first_initial = first_name[0]
        last_initial = last_name[0]
        combo = str(first_initial.upper() + last_initial.upper())
        #combo = combo + " "


        #for i in range(num_names):
        #initial_list = [initial]



        #print(first)



def main():
    #name_reverse()
    #company_name()
    #initials()
    names()
    # add other function calls here


main()
