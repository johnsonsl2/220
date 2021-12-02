"""
Name: Sara Johnson
sales_force.py

Problem: Create class for the data for a sales force

Certification of Authenticity:
I certify that this assignment is entirely my own work

"""

from sales_person import *

class SalesForce:
    def __init__(self):
        SalesPerson.__init__(self)
        self.sales_people = []  # list of SalesPerson
        self.sales_people.append(SalesPerson)

    def add_data(self, file_name):
        infile = open(file_name, 'r')
        for line in infile:
            self.sales_people.append(SalesPerson.__str__())
        infile.close()

    def quota_report(self, quota):
        return list[list[SalesPerson.get_id(), SalesPerson.get_name(), SalesPerson.total_sales(), SalesPerson.met_quota(quota)]]

    #def top_seller(self)

    def individual_sales(self, employee_id):








def main():
    SalesForce.add_data('salesData2')

main()