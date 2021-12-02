"""
Name: Sara Johnson
sales_person.py

Problem: Create class for the data for a sales person

Certification of Authenticity:
I certify that this assignment is entirely my own work

"""

class SalesPerson:

    def __init__(self, employee_id, name):
        #employee_id should be the ID number in form of an int
        #name should be a string of the person's full name
        self.sales = []
        #sales is a list of floats that represents the mount of each sale

        self.employee_id = employee_id
        self.name = name

    def get_id(self):
        #returns the employee id
        return int(self.employee_id)

    def get_name(self):
        #returns the employee's name
        return str(self.name)

    def set_name(self, name):
        # sets the name of the employee
        self.name = name

    def enter_sale(self, sale):
        #add a sale number to the list
        self.sales.append(sale)

    def total_sales(self):
        #returns the sum of a person's sales
        return float(sum(self.sales))

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if quota >= self.total_sales():
            return True
        elif quota <= self.total_sales():
            return False

    def compare_to(self, other):
        #other should be another SalesPerson
        if other.total_sales() > self.total_sales():
            return -1
        elif other.total_sales() < self.total_sales():
            return 1
        elif other.total_sales() == self.total_sales():
            return 0

    def __str__(self):
        return str(self.employee_id) + '-' + self.name + ':' + str(self.total_sales())





