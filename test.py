# c = input("Enter a single character:")

# if c in 'aeiouAEIOU':
#     print("Its a vowel....")

# elif c in '0123456789':
#     print('Its a digit...')

# elif c in '~!@#$%^&*()_+{}|?><':
#     print('Its a special char')

# else:
#     print('its a consonant')



"""Leap year"""

# year = int(input("Enter year:"))


# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print("It is a leap year...")

# else:
#     print("Not a leap year....")




"""Second largest"""


# x = int(input("Enter the first number :"))
# y = int(input("Enter the second number :"))
# z = int(input("Enter the third number :"))

# largest = 0
# second = 0

# if x > y and x>z:
#     largest = x

#     if y > z:
#         second = y
#     else:
#         second = z

# elif y > x and y > z:
#     largest = y

#     if x > z:
#         second = x
#     else:
#         second = z

# else:
#     largest = z

#     if  x > y:
#         second = x
#     else:
#         second = y

# print("Second largest number is",second)


# company = "Quest"


# for a in company:
#     print(a)

# for s in "sreeraj":
#     print("hi")

# for i in :
#     print('sree')


# for i in range(5,20,20):
#     print(i)



# for i in range(5):
#     for j in range(5):
#         print(j,end=" ")
#     print()



# for i in range(9):
#     if i == 3:
#         break

#     print(i)


"""dictinoary"""


# empty_dict = {}
# print(type(empty_dict))

# empty_dict2 = dict()
# print(type(empty_dict2))

# students = { 1 : 'amjith', 2 : 'vismaya', 3 : 'sreeraj', 1 : 'alan'}
# print(students)

# course = { 'A':'python', 'B':'JAVA', 'c':'JS'}
# print(course)

# print(course['B'])

# check = { {1 :1 , 2 : 2} : 1, 2:2, 3:3}

# """Key Check list - > int, str, float, tuple"""
# print(check)


# value_check = { 1 : {1 : 10, 2 : 20}, 2 : 2 , 3 : 3}
# print(value_check)


# marks = { 'maths' : 95, "chemistry" : 85, "science" : 90}
# print(marks)

# marks["malayalam"] = 100

# print(marks)

# marks["maths"] = 80
# print(marks)


# marks.update({'English': 100, 'IT' : 100})
# print(marks)

# list1 = [10,20,30]

# print(dir(list1))

# print(dir("Quest"))


# d = { "fruits" : ['apple', 'banana'], 'price' : "Ten Rupees"}
# print(d['fruits'])

# d['fruits'].append('mango')

# print(d)

# print(d['price'].upper())


# marks = { 'maths' : [95, 100], "chemistry" : 85, "science" : 90}


# keys = ['name', 'age', 'place', 'phone']

# new_dict = dict.fromkeys(keys, "unknown")

# print(new_dict)



# copy_dict = marks.copy()

# print(copy_dict)

# copy_dict['maths'].append(90)

# print(copy_dict)

# print(marks)








# marks.clear()


# print(marks)
# print(marks.popitem())

# print(marks.popitem())
# marks.popitem()

# marks.pop('chemistry')

# del marks["malayalam"]

# print(marks)


# print(marks["maths"])

# print(marks.get("malaylam"))

# print(marks.keys())

# print(marks.values())

# print(marks.items())

# for k in marks.items():
#     print(k)



# student = { 'name' : 'amjith', 'course' : 'python'}

# result = student.setdefault("city", "Kochi")

# print(result)

# print(student)



# s = "Python"

# for i in range(len(s)):
#     print(s[i])



# print(s[ 0 : 3])
# print(s[ 2 : 5])

# print(s[ 0 : ])
# print(s[  :  : 2])

# print(s[ : : -1])

# print(s[-1 : -4 : -1])



# s = "malayalam"

# print(dir(s))

# reverse = s[ : : -1]

# if s == reverse:
#     print("palindrome")
# else:
#     print("not")



# s = 'python'

# print(s.upper())

# print('PYTHON'.lower()) 

# print("my name is sree".title())

# print("this is a sentence".capitalize())

# print("THIS is A swap CASE example".swapcase())



"""searching and finding"""


# sentence = "This is a test sentence"

# print(sentence.find('i'))
# print(sentence.rfind('i'))

# print(sentence.index('i'))
# print(sentence.rindex('i'))

# print(sentence.count('t'))


"""validation"""


# print("ABC".isalpha())
# print("2356".isdigit())

# print("ABC235".isalnum())

# print("        ".isspace())

# print("ABC2356".isupper())

# print("abc253---".islower())

# print("My Name Is Sreeraj".istitle())

# print("My Name Is Sreeraj".startswith("My Name"))

# print("My Name Is Sreeraj".endswith("Sreeraj"))

# print("sreeraj@gmail.com".endswith('@gmail.com'))



"""modification and replacement"""

# print("Python is a high level prgrming language. Python supports multiple programming paradigm.".replace(" ","-",2))


# print("---------------------sree   raj--------------------------".strip('-'))
# print("---------------------sree   raj--------------------------".lstrip('-'))
# print("---------------------sree   raj--------------------------".rstrip('-'))



"""spliting and joining"""


# string = "adhi,malavika,harshadh,sreeraj"

# result = string.split(',')

# print(result)


# joined_string = "=".join(result)

# print(joined_string)



# names = input("Enter student names seperated by Comma:")


# splited = names.split(',')

# print(splited)

# joined = " ".join(splited)

# print(joined)


# """escape sequence"""

# print("Python\rJava")




"""Data Structures"""
# empty_list = [ ]
# print(type(empty_list))


# empty_list2 = list()
# print(type(empty_list2))


# students = ['malavika','harshadh','adhi',25,True,25.25, 25,True]
# print(students)
# print(len(students))


# print(students[2])
# print(students[-3])

# print(students[ : : -2])


# for s in students:
#     print(s)



# sample = [2,3,5]

# print(3 in sample)

# sample2 = [2,3,5]

# print(sample == sample2)

# print(id(sample2))
# print(id(sample))

# print(sample is sample2)


# sample *= 3

# sample += [200,300,500]

# sample += 'Quest'

# print(sample)



# numbers = [200,900,800,300,600,500,600]

# total = sum(numbers)

# print(total)

# print(max(numbers))

# print(min(numbers))











# sample = [3000,9000]

# sample.extend(numbers)

# print(sample)



# numbers.sort(reverse=True)

# print(numbers.count(600))


# copy_list = numbers.copy()

# print(copy_list)


# numbers.clear()

# numbers.remove(500)

# numbers.pop()

# print(dir(numbers))

# numbers.append(700)
# numbers.insert(3,800)
# print(numbers)




# numbers = [20,30,50, [200,300,500,[2000,3000,5000,6000,8000]]]

# print(numbers[3][3][3])



# for i in range(20):
#     numbers.append(i)



# student = { 'id' : 202, 'name' : 'sree', 'course' : 'python', 2 : 'int', 20.25 : 'float',(20,30):'tuple', True:'True'}
# print(student)

# print(student['name'])
# print(student['age'])


# fruits = { 'A' : 'Apple', 'B':'Banana','C': 'Chikku'}

# # fruits.pop('A')

# fruits.popitem()

# print(fruits)






# fruits.update({'M':'Mango', 'P':'pineapple'})
# print(fruits)

# print(fruits['B'])

# print(fruits.get('x'))


# fruits['D'] ="Dragon Fruit"
# print(fruits)

# fruits['A'] = 'Anaar'
# print(fruits)

# for k,v in fruits.items():
#     print(k,v)




# students = {
#     202 : {'name':'Adhi','course':'Python','marks': [95,30,78]},
#     203 : {'name':'Maalu','course':'JAVA'}
# }

# print(students[202]['marks'])

# students[202]['marks'].append(200)

# print(students[202])





# numbers = {}

# for i in range(1,11):
#     numbers[i] = i**2

# print(numbers)

# square = { i : i**2 for i in range(1,11)}

# print(square)



# strings = ['adhi', 'maalu', 'harshadh', 'sreee']

# lenDict = { i : len(i) for i in strings }
# print(lenDict)

# print(list(lenDict.values()))



# numbers = [20,3,8,9,5,3,5,8,5,625,52,5]

# evenOdd = { i : 'Even' if i % 2 == 0 else 'ODD' for i in numbers}
# print(evenOdd)

# evenSquare = { i : i**2 for i in numbers if i % 2 == 0}

# print(evenSquare)



# def greet(name):
#     print(f"Welcome {name}")


# greet('adhi')
# greet('harshadh')
# greet('malavika')




# def get_details(name, age, place):
#     print(f"Name : {name}\nAge : {age}\nPlcae : {place}")


# name = input("Enter Your name:")

# age = input("Enter your age:")

# place = input("Enter Your place:")


# get_details(name,age, place)



# def get_details(name='malavika',age=20):
#     print(f"Name: {name}\nAge : {age}")


# get_details('adhi',30)




# def add(*args, **kwargs):
#     print(args)
#     print(kwargs)

# add(20,30, x= 80,y =90)



# def to_upper(s : str)->str:
#     """This function recieves a string - s and returns its uppercase format"""
#     print(s.upper())

# to_upper('adhi')


# def add(x : int, y : int)->int:
#     print(x+y)





# def add(a, b):
#     """
#     This function adds two numbers and returns the result.
    
#     Parameters:
#         a (int/float): First number
#         b (int/float): Second number

#     Returns:
#         int/float: Sum of a and b
#     """
#     return a + b

# print(add.__doc__)





# file = open(r"C:\Users\HP\OneDrive\Desktop\Python_Conditional_Statements_Lab_Questions.txt",'r')

# """read content"""

# data = file.read()
# print(data)

# # file.write("New data inserted")
# # file.write("Quest innovative solutions")

# file.close()



# with open("Python_If_Conditional_Lab_Questions.txt",'w') as file:
#     # print(file.read())
#     file.write("data")



# with open("exam.txt",'w') as f:
#     f.write("Exam data")

# with open("python_learnings.py",'w') as p:
#     p.write("name = \"sree\"")


# with open("test_file.txt", 'r') as f:
#     f.read()


# with open("exam.txt", 'r+') as f:
#     print(f.tell())
    
#     # print(f.seek())
#     # print(f.read())
#     f.write("New data")
#     f.write("\nQuest innovative solutions")
    
#     f.write("Test data")
#     print(f.tell())
#     print(f.read())



# with open("python_learnings.py",'r+') as f:
#     print(f.tell()) # 0
#     print(f.read())
#     print(f.tell()) # last index
#     print(f.read()) # empty string

#     f.seek(0)
#     print(f.tell()) # 0
#     print(f.read())




# with open("exam.txt", 'w+') as f:
#     print(f.tell())

#     print(f.read())


# with open('zzzzzzzzzzzz.txt','w+') as f:
#     print(f.tell())

    # f.write("Write + read mode")

    # print(f.tell())

    # print(f.read())

    # f.seek(0)
    # print(f.read())



# with open("students.txt", 'a+') as f:
#     print(f.tell())
#     print(f.write("vismaya"))
#     print(f.tell())

#     f.seek(0)
#     print(f.read())


# with open("studentsNew2.txt",'x+') as file:
#     file.write("Sample text..")
#     file.seek(0)
#     print(file.read())




# with open('DA.py','rb') as f:
#     print(f.read())


# with open('Tony Stark_ Cinematic Marbled Poster.png','rb') as f:
#     print(f.read())


# students = ['\njoshua\n','hari\n','jhon']


# with open('exam.txt','a+') as file:
#     # file.write(students)
#     file.writelines(students)


#     # print(file.readable())
#     # print(file.writable())
#     # print(file.seekable())

#     # print(file.read())
#     # data = file.read()
#     # print(data)
#     # print(file.readline(6))
#     # print(file.readline())
#     # print(file.readline())

#     # print(file.readlines(10))


""" inbuilt file method
1.read()
2.write()
3.readline()
4.readlines()
5.writelines()
6.seek()
7.tell()
8.readable()
9.writable()
10.seekable()
11.close()
"""

# with open('exam.txt','r+') as file:
#     print(file.readlines(30))





# def add(x, y):
#     return x+y
    



# print(add(20,30))

# result = add(20,30)

# print(result)




# def check(value):
#     if value % 2 == 0:
#         return "even"
#     else:
#         return "Odd"

# result = check(20)
# print(result)

# print(check(20))


# def fact(n):
#     if n == 1:
#         return 1

#     return n * fact(n-1)


# print(fact(5))



# def count(n):
#     if n == 0:
#         return

#     print(n)

#     return count(n-1)

# count(5)



# def add(x , y):
#     return x + y

# total = lambda a,b: a+b

# print(total(5,2))



# even_odd = lambda n : "even" if n % 2 == 0 else "Odd"

# print(even_odd(25))
# print(even_odd(20))



def add(x,y):
    return x+y


def multiply(x,y):
    return x*y

def subtract(x,y):
    return x-y


def calculate(x,y,func):
    return func(x,y)


print(calculate(20,30,add))

print(calculate(20,30,multiply))

print(calculate(20,30,subtract))

