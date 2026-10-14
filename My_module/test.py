# import constants

# print(constants.company)

# print(constants.pi)


# import calculations

# x = 20

# y = 25

# print(calculations.add(x, y))

# print(calculations.multiply(x,y))


# import constants

# import calculations


# calculations.multiply()

# calculations.add()

# from calculations import *

# add()

# pi


# print(add(30,20))

# print(substract(20,10))

# print(pi)


# from constants import pi as cpi
# from calculations import pi as capi

# print(cpi)

# print(capi)



# import calculations

# calculations.pi

# from calculations import add

# add()

# from calculations import * 

# add()

# multiply()

# from calculations import pi as cpi, add as sum



"""math module"""


# import math


# print(math.pi)


# print(math.sqrt(25))
# print(math.sqrt(100))

# print(math.pow(10,2)) # 10**2

# print(math.pow(2,10)) # 2**10

# print(math.factorial(5))
# print(math.factorial(6))

# print(math.ceil(3.8))
# print(math.ceil(3.2))

# print(math.floor(3.8))
# print(math.floor(3.2))


# print(math.trunc(4.6))
# print(math.trunc(4.999))
# print(math.trunc(4.001))

# print(math.fabs(-25.25))
# print(math.fabs(25.25))

# print(abs(-259))





"""Date time module"""

# from datetime import date, time, datetime, timedelta

# y = int(input("Enter your birth year:"))
# m = int(input("Enter your birth Month:"))
# d = int(input("Enter your birth day:"))

# dob = date(y,m,d)

# today = date.today()


# difference = today - dob

# print(f"Days lived : {difference.days}")

# print(f" Age = {difference.days / 365}")



# today = date.today()
# print(today)

# future_date = today + timedelta(days=10)
# print("After 10 days",future_date)

# previous_date = today - timedelta(days=10)
# print("Before 10 days:", previous_date)


# now = datetime.now()

# print(now)

# print(now.strftime("%a/%b/%y"))
# print(now.strftime("%I- %M- %S- %p"))


# now = datetime.now()
# print(now)

# print(now.year)
# print(now.hour)
# print(now.microsecond)


# event = datetime(2026,11,5, 6, 30, 15)
# print(event)

# t = time(15,30,45)
# print(t)

# print(t.hour)
# print(t.minute)
# print(t.second)
# print(t.microsecond)


# class_time = time(18,30,00,00)

# print(f"Class starts at {class_time}")




# today = date.today()

# print(today)

# print(today.year)
# print(today.month)
# print(today.day)

# print(today.weekday())

# new_date = today.replace(year=2001, month=11, day=5)
# print(new_date)



"""Random Module"""

import random

# print(random.random())

# print(random.randint(1,10))

# print(random.randrange(1,5,2))

# print(random.uniform(1,5))


students = ['alan','alisha','amjith','raana','vismaya']

random.shuffle(students)

print(students)

# print(random.choice(students))

# print(random.choices(students,k=10))

# print(random.sample(students,k=3))