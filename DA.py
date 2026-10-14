# email = 'quest.co.in'

# print('Welcome')

# print('email')

# print('✅')

# print(2526)

# num = 20

# print(num)

# students = 'Nivin'

# print(type(students))

# number = 25268963.258

# print(type(number))

# a = 20

# b = 25

# print(id(a))

# print(id(b))


# x = 20

# y = 26

# result = x / y

# print(result)

# num% = 200

# x = 50

# y = 25

# result = x + y

# difference = y - x

# product = x * y

# print("Sum =",result)

# print("difference =", difference)


# print("Product =", product)


# name = 'ammu'

# age = 25

# place = 'Kottayam'

# print("my name is",name,"i'm",age,"years old. and i'm from", place)

# name = 'Athul'

# print("my name is",name,"i'm",age,"years old. and i'm from", place)

# print(name)


# x = 'ABC-'

# y = 5

# print( x * y )


# name = input("Enter your name:")

# age = input("Enter your age:")

# place = input("Enter your place:")

# print("my name is",name,"i'm ",age,"years old","i'm from",place)






# name = input("Enter your name:")

# print("Your name is",name)

# print(type(name))

# phone = int(input("Enter your phone number:"))
# print(phone)
# print(type(phone))

# a = 250

# print(type(a))

# a = str(a)
# print(type(a))


# x = int(input("Enter first number:"))

# y = int(input("Enter second number:"))

# result = x + y

# print("Sum =",result)




"""Comparison operator"""

# x = 25

# y = 250

# print(x != y) 




"""assignment operator"""

# x = 20

# y = 5

# x /= y


# print(x)

# print(y)





# name = "nasif"

# print('as' not in name)




# x = 20

# y = 200


# print(id(x))

# print(id(y))

# print(x == y)
# print(x is y)



# print(20 > 5 or 5 < 8 or "ABC" == "ABC")


# print( not( 50 < 5 ))

# print(True or False and False)





# t = (5,'sree',25.2, [200,300])

# print(type(t))

# print(t[2])
# print(t[3][0])

# print(t[::-1])


# t = (2,35,8,9,2,5,8,9,2,7,5,85,8,2,8,5852,85,2)
# print(t.index(8,8))




# age = int(input("Enter your age:"))

# if age >= 18:
#     print("You are eligible for voting")
# else:
#     print("You are not eligible..")



# number = int(input("Enter a number:"))

# if number > 0:
#     print("positive")
# else:
#     print("Negative/Zero")

# if number < 0:
#     print("Negative")
# else:
#     print("Postive/Zero")

# if number == 0:
#     print("Zero")
# else:
#     print("Postive/negative")




# if number > 0:
#     print("positive")
# else:
#     print("negative")

# if number % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")



# num = int(input("Enter a number:"))

# if num > 0:
#     print("Postive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")




# """Grade System"""
# mark = int(input("Enter your mark:"))

# if mark > 100 or mark < 0:
#     print("Enter a valid mark...")

# elif mark > 90:
#     print("A Grade")

# elif mark > 80:
#     print("B Grade")

# elif mark > 70:
#     print("C Grade")

# elif mark >60:
#     print("D grade") 

# else:
#     print("Failed")



# username = 'sreeraj_mathiyath'
# password = 'sree6585'


# u_name = input("Enter your user name:")
# u_pass = input("Enter your password:")


# if u_name == username:
#     if u_pass == password:
#         print("Login Successful....")
#     else:
#         print("Incorrect password...")
# else:
#     print("Invalid username...")


# name = 'nasif'

# for i in range(5):
#     mark = int(input("Enter your mark:"))


# numbers = range(20)
# print(numbers)



# company = 'Qis'

# print(len(company))

# for i in company:
#     print(i)


# number = 23569
# for i in number:
#     print(i)



# for i in range(10,0,-2):
#     print(i)


# name = 'sree'

# for i in name:
#     print(name)


# comapny = "QIS"

# for i in comapny:
#     print(i)



# limit = int(input("Enter your limit:"))

# for i in range(1, limit+1):
#     if i % 5 == 0:
#         print(i)


# for number in range(1,11):
#     print(number**2)



# value = int(input("Enter a value:"))

# for i in range(1,11):
#     print(f"{i} * {value} = {i*value}")


# import My_module.calculations

# print(My_module.calculations.add(20,80))


# for i in range(1,21):
#     print(i)


""" print integers from 1 to 20"""
# i = 1

# while i <= 20:
#     print(i)
#     i += 1



"""Print intergers upto a limit"""

# value = 0
# limit = int(input("Enter a limit:"))

# while value<= limit:
#     print(value)
#     value += 1





# limit = int(input("Enter a limit:"))

# for i in range(limit+1):
#     print(i)




"""print integers from 20 - 0"""
# i = 20

# while i > 0:
#     print(i)
#     i -= 1
    


# for i in range(1,11):
#     print(f"{i} * 2 = {i*2}")


"""Multiplication table using while loop"""

# value = int(input("Enter a value:"))

# i = 1

# while i <= 10:
#     print(f"{i} * {value} = {i*value}")
#     i += 1


"""Sum of first 10 integers"""

total = 0 # 0 + 1 = 1, 1 + 2 = 3, 3 + 3 = 6, 6 + 4 =10

for i in range(1,11):
    total += i # total = total + i

    print(total)