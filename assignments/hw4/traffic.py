"""
Name: Sara Johnson
mean.py

Problem: Write a program to calculate traffic patterns

Certification of Authenticity:
I certify that this assignment is entirely my own work

"""

def main():
    print("Please enter the asked for values to calculate traffic patterns")
    num_roads = eval(input("How many roads were surveyed?"))
    sum_cars_final = 0
    for i in range(1, num_roads + 1):
        days_statement = "How many days was road " + str(i) + " surveyed?"
        days = eval(input(days_statement))
        sum_cars = 0


        for b in range(1, days + 1):
            car_days_statement = "How many cars traveled on day " + str(b) + "?"
            cars = eval(input(car_days_statement))
            sum_cars = sum_cars + cars

        day_ave_pre = sum_cars / days
        day_ave = round(day_ave_pre, 2)
        print("Road", i, " average number of vehicles per day: ", day_ave)
        sum_cars_final = sum_cars_final + sum_cars
    total_ave_pre = sum_cars_final / num_roads
    total_ave = round(total_ave_pre, 2)
    print("Total number of vehicles traveled on all roads: ", sum_cars_final)
    print("Average number of vehicles per road: ", total_ave)


if __name__ == '__main__':
    main()






