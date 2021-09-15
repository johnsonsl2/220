"""
Name: <Sara Johnson>
<interestmessup.py>

Problem: Calculate the monthly interest charge on a credit card account

Certification of Authenticity:
I certify that this assignment is entirely my own work

"""

def interest():
    print("Let's calculate the monthly interest charge on your credit card")
    annual_rate = eval(input("What is your annual interest rate(not a percent)?"))
    billing_cycle = eval(input("How many days are in the billing cycle?"))
    previous_balance = eval(input("What is your previous balance(without interest)?"))
    payment_amount = eval(input("What is the payment amount?"))
    payment_day = eval(input("What day of the billing cycle was the payment made?"))
    remaining_day = billing_cycle - payment_day
    print(remaining_day)
    monthly_rate = (annual_rate / 12) / 100
    print(monthly_rate)
    x = previous_balance * billing_cycle
    print(x)
    y = payment_amount * remaining_day
    print(y)
    z = x - y
    print(z)
    ave = z / billing_cycle
    print(ave)
    monthly_charge = ave * monthly_rate
    print("This is your monthly interest charge: $", monthly_charge)


if __name__ == '__interest__':
    interest()
