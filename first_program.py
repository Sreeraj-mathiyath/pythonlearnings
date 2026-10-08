# print("Hello welcome to your first python class")

# print('This is a message.....')

# """this is a 
# multi line 
# comment"""




# """this a function that recieves two integer values a and b.
#  and returns their sum"""
# def add(a,b):
#     return a + b # must return a non empty value

# print(add(258966,2588))




# name = "Sreeraj"
# age = 25
# stack = 'python'

# print(name,age,stack)

# print(type(name))
# print(type(age))
# print(type(stack))

# print(id(name))
# print(id(age))
# print(id(stack))


# name = "abhi"
# place = "calicut"
# age = 25

# print("My name is",name,"And i'm from",place)

# print(f"My name is {name} and \ni'm from {place}. \ni'm {age + 5} years old")





# name = input("Enter your name :")
# age = int(input("Enter your age:"))
# place = input("Enter your place:➡️")

# print(f"your name is {name}, {age} years old and from {place}")


# number = 25896
# print(type(number))

# converted = str(number)
# print(converted)
# print(type(converted))



# name = "sreeraj"
# print(name)
# print(id(name))

# name = "adhi"
# print(name)
# print(id(name))



"""-----------------------operators-----------------------------"""

# a = input("Enter your first number:")
# b = input("Enter your second number:")

# print(int(a) + int(b))

# print("abc" + 5)



# x = int(input("Enter first number:"))
# y = int(input("Enter second number:"))
# print( x ** y)



"""comparison operators"""
# a = 20
# b = 25

# print(a == b)

# print("abc" == "Abc")
# print("20" == 20)


# a = 20
# b = 25
# print(a != b)
# print("20" != 20)

# a = 25
# b = 25

# print(b >= a)


# print("A" < "a")
# # print(len("abc"))
# print(ord("A"))
# print(ord("a"))

# print(chr(67))


# a = 20
# b = a
# c = 20

# print(a)
# print(b)

# print(id(a))
# print(id(b))
# print(id(c))


# a = 20
# b = 20
# print(a)
# print(b)

# b += a
# print(f"value of b after assignment operation = {b}")

# x = "sree"
# y = "raj"
# print(y)

# y += x 
# print(y)


# x = 20
# y = 5

# x **= y
# print(x)


# name = 'sreeraj'

# for i in name:
#     print(i)

# phone = 6238968952

# for i in phone:
#     print(i)




# print("Abc" not in "abcdef")


# print(50 in 2050)


# a = 20
# b = 25

# print(id(a))
# print(id(b))

# print(a == b)
# print(a is b)


# a = 20
# b = 20


# x = [2,3,5]
# y = [2,3,5]

# print(a == b) 
# print( x == y)

# print(a is b)
# print(x is y)


# s1 = "ABC123@!#$%❤️"
# print(type(s1))

# print("ഹലോ...")


# name = 'alan'
# print(name, id(name))

# name = 'alisha'
# print(name, id(name))
# print(len(name))

# print(len("     "))

# for i in "calicut":
#     print(i)

# print("नमस्ते")



# company = "Quest"
# # print(len(company))

# # print(company[0])
# # print(company[1])
# # print(company[2])
# # print(company[3])
# # print(company[4])
# # print(company[5])

# print(company[-1])
# print(company[-2])
# print(company[-3])
# print(company[-4])
# print(company[-5])
# print(company[-6])


# stack = 'python full stack'

# for i in stack:
#     print(i)

# for i in range(1,len(stack)+1):
#     print(stack[-i])



# print(len(stack))
# print(stack[6])
# print(stack[5])
# print(stack[16])
# print(stack[-1])



# designation = "Back-End Developer"

# print(designation[0:5])
# print(designation[0:len(designation)])
# print(len(designation))
# print(designation[0:-1])
# print(designation[0:])
# print(designation[0:25])


# print(designation[0 : len(designation) :2])

# print(designation[ : : 2])

# print(designation[-5 : -1])
# print(designation[-1 : -5 : -1])

# print(designation[ : : -1])

# print(designation[5 : ])

# name = 'sreeraj'
# print(name[ : : -1])

# print(name[-6 : -1])

# print(designation[5])
# print(designation[-3])
# print(designation[8])
# print(designation[8])
# print(designation[10])



# stack = "python"

# for i in stack:
#     print(i)

# for i in range(len(stack)):
#     print(stack[i])


# for i,v in enumerate(stack):
#     print(i,v)

# print(list(enumerate(stack)))


# stack = 'python'
# language = 'MALAYALAM'

# """case conversion"""

# print(stack.upper())
# print(language.lower())
# print("my name is sreeraj".title())
# print("my name is sreeraj".capitalize())

# print('Python'.swapcase())
# print('MaLaYaLaM'.swapcase())


"""searching and finding"""


# print("Hello".find('l'))
# print("malayalam".find('malayalam'))
# print("malayalam".find('z'))


# print("malayalam".find('a'))
# print("malayalam".rfind('a'))

# print("Quest".find('e'))
# print("Quest".index('e'))

# print("Quest".find('Z'))
# print("Quest".index('Z'))

# print("malayalam".index('l'))
# print("malayalam".rindex('l'))

# print("malayalam".count('ala'))



"""validation and checking"""

# print("Quest".isalpha())

# print("1234567890".isdigit())

# print("Quest123".isalnum())

# print("                  ".isspace())

# print("QUEST123@ ❤️".isupper())

# print("quest123$ ➡️".islower())

# print("My Name Is Sreeraj".istitle())


# print("Python".startswith('Py'))

# print("img.png".endswith('.png'))

# print("http://www.google.com".startswith('http'))



"""Modification"""


# print("Python".replace('th','TH'))

# s = "Python"
# print(id(s))

# s = s.replace('th','TH')

# print(s)
# print(id(s))


# print("python python python python python".replace('python','AI',2))

# print("My name is amjith".replace('was','is'))


# company = '*************************Qu*******est******************************'

# company = company.strip('*')

# print(company)


# print("Mr.Amjith".removeprefix('Mr.'))
# print('sreeraj M R'.removesuffix('M R'))



"""Formatting...."""

# print("Quest".center(10))

# s = "Quest"
# print(len(s))
# s = s.center(11,'-')

# print(s)
# print(len(s))



# print("Quest".ljust(20,'-'))
# print("Quest".rjust(20,'-'))

# print("Q".zfill(10))



# print("My name is {name}. i'm {age} years old".format(age=24,name ='sreeraj'))

# name = 'sreeraj'
# age = 24

# print(f"my name is {name.upper()}. i'm {age+10} years old")

"""split"""


# test = "a-b-c-d"

# splited_string = test.split('-')

# print(splited_string)


# print("My name is amjith".split())

# print("malayalam".split('a'))
# print("malayalam".split('W'))

# print('malayalam'.split('a',2))

# print("malayalam".rsplit('a',2))


# string = "my name is amjith"

# splited_string = string.split()

# print(splited_string)

# joined_string = '-'.join(splited_string)
# print(joined_string)

# test_string = "sreeraj"
# test_string2 = "AAAA"

# result = test_string.join(test_string2)
# print(result)
# result = ' '.join([test_string,test_string2])
# print(result)


# print("name = sree = raj".partition('='))
# print("name = sree = raj".rpartition('='))



# print("A B C D E F G".split(" ",2))
# print("A B C D E F G".rsplit(" ",2))


# print("First\nLine.\nsecond\tline \\ \' \" \rtest")


# # print("second line")


# print("test string \r r string")

# s = 'sreeraj'
# print(s[::-1])




"""List"""


# empty = [ ]
# print(type(empty))

# empty_list2 = list()
# print(type(empty_list2))

# students = ['amjith','aleesha','vismaya','alan','rana',25029]
# # print(students)
# # print(len(students))

# # details = [1,'sreeraj',24.7,True,1,1,True,24.7]
# # print(details)

# for s in students:
#     for x in s:
#         print(x)


# s = 'alisha'
# print(s[1])

# fruits = ['apple','banana','mango','orange']
# print(fruits[2])
# print(fruits[-2])

# print(fruits[0:3])
# print(fruits[0:])

# print(fruits[-4:-2])

# print(fruits[::-1])

# print(reversed(fruits))

# print(list(reversed(fruits)))

# students = ['amjith','aleesha','vismaya','alan','rana']

# for s in students:
#     print(s)

# for s in range(len(students)):
#     print(students[s])

# for i,s in enumerate(students):
#     print(i,s)


# a = [1,2]
# b = [3,4]

# c = a + b
# print(c)

# a += [3]
# print(a)

# b += 'alisha'
# print(b)


# a = [1,2,3,4]
# print(id(a))

# a += [5]
# print(id(a))
# print(a)




# a = [1,2,3,4,5]
# b = [1,2,3,4,5]

# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))

# a = [1,2,3,4,5]
# b = a
# print(a)
# print(b)

# b += [6]
# print(b)
# print(a)

# print(a == b)
# print(a is b)

# x = (1,2,3)
# y = x

# print(x)
# print(y)


# y = list(y)
# y += [4]
# y = tuple(y)
# print(y)
# print(x)


# a = [1,2,3]
# b = [1,2,3]

# b = a



# s = 'sree'
# t = s
# print(s)
# print(t)

# t += 'mr'
# print(t)
# print(s)


# a = [1,2,3]
# b = a

# print(a is b)

# print(a)
# print(b)

# b+=[4]

# print(b)
# print(a)

# a= [1,2]
# b= [1,2]

# print(a is b)

# print(1 in a)


# s = "hello"
# s = s.encode()

# print(s)

# s = s.decode()
# print(s)





# purchase_amount = 500

# if purchase_amount > 1000:

#     if purchase_amount > 5000:
#         print(f"discount 25% applied. discount amount {purchase_amount * 0.25}")

#     else:
#         print(f"discount 5% applied. discount amount {purchase_amount * 0.05}")
# else:
#     print("No discount...")



# for i in range(20):
#     if i == 5:
#         break
#     print(i)
# else:
#     print("Loop completed")


# num = int(input("Enter a number:"))


# for i in range(1,11):
#     print(f"{i} * {num} = {i*num}")


# limit = int(input("Enter a limit:"))
# count = 1

# for i in range(1,limit):
#     if i % 2 == 0:
#         count *= i

# print(count)

# for i in range(2,limit+1):
#     print(f"{i} - {i**3}")



"""List methods..."""

students = ['alisha','amjith','alan','Vismaya','vismaya','alisha','abc','ABC','XYZ']

# print(len(students))

# print(min(students))

# print(max(students))

# test = sorted(students)

# print(test)

# rev = list(reversed(students))
# print(rev)


# numbers = [2,5,]

# result = sum(numbers)
# print(result)



# print(min(numbers))
# print(max(numbers))


# students.reverse()

# print(students)


# students.sort()

# print(students)

# print(ord('A'))
# print(ord('a'))

# numbers = [25,7,8,9,3,6,47,5,8]
# numbers.sort(reverse=True)
# print(numbers)




# print(students.count('alisha'))

# print(students.count('sree'))


# students2 = ['sree']

# students2.extend(students)

# print(students2)

# students2.extend('Quest')
# print(students2)

# print(students.index('sree'))


# copy_students = students.copy()
# print(copy_students)

# copy_students.append('sree')
# print(copy_students)
# print(students)

# students.clear()
# print(students)


# students.remove('alisha')
# print(students)

# students.pop(20)
# print(students)

# students.pop()
# print(students)

# students.pop()
# print(students)

# students.append('sreeraj')
# print(students)

# students.append(['rana','sibin'])
# print(students)

# students.append(2026)
# print(students)

# students.insert(2,'ammu')
# print(students)

# students.insert(20,'abhi')
# print(students)

# students.insert(-2,'jhon')
# print(students)



"""nested list"""

# numbers = [1,2,3, [4,5,6], [7,8,9]]



# print(numbers)

# print(len(numbers))

# print(numbers[3][1])
# print(numbers[-1][-1])



# numbers = [[1,2,3,4], [10,20,30, [40,50,60]], [6,7,8,9]]

# print(len(numbers))

# print(numbers[1][3][1])

# print(numbers[-2][-1][-2])


# matrix = [ [1,2,3], [4,5,6], [7,8,9] ]

# for m in matrix:
#     for i in m:
#         print(i, end=" ")
#     print()


# numbers = [1,2,3, [10,20,30]]

# copied = numbers.copy()

# copied[-1].append(40)

# print(copied)

# print(numbers)


# pin = "2526"

# i = 0

# while i < 3:
#     user_input = input("Enter your pin number:")

#     if user_input == pin:
#         print("Success....")
#         break

#     else:
#         i+= 1
#         print("Incorrect pin try again..")
#         continue
   
# else:
#     print("card is blocked..")



# number = int(input("Enter a number:"))

# fact = 1

# i = 1

# while i <= number:
#     fact *= i
#     i += 1

# print(f"factorial of {number} = {fact}")


# number = int(input("Enter a number:"))

# reverse = 0

# while number > 0:
#     digit = number % 10
#     reverse = reverse * 10+ digit
#     number //= 10

# print(reverse)

# sample_list = []

# for i in range(1,11):
#     sample_list.append(i)

# print(sample_list)

# list_comprihension = [ i for i in range(1,11) ]

# print(list_comprihension)

# square = [ i**2 for i in list_comprihension ]
# print(square)


# students = ['amjith','alan','alisha','vismaya']


# uppercase = [ s.upper() for s in students ]

# print(uppercase)

# numbers = [ i for i in range(1,21) ]

# print(numbers)

# even = [ i for i in numbers if i % 2 == 0  ]
# print(even)



# students =['amjith','alan','alisha','vismaya','sreeraj','abhi','vishak','athul','vipin']

# filter_students = [ s for s in students if s[0] == 'a' ]
# print(filter_students)


# numbers = [i for i in range(1,21)]

# list1 = [ i**2 if i % 2 == 0 else i**3 for i in numbers ]
# print(list1)

# sample_list = [25,8,9,32,36,45,75,25,10,1,5,7,10]

# list2 = [ i if i % 5 == 0 else 0 for i in sample_list ]
# print(list2)



# empty_tuple = ()
# print(type(empty_tuple))

# sample_tuple = ('Quest',2026, 8.25, True,2026)
# print(sample_tuple)

# print(len(sample_tuple))


# print(sample_tuple[2])

# sample_tuple = (5,)
# print(type(sample_tuple))
# print(len(sample_tuple))

# empty = tuple()
# print(type(empty))

# t1 = (2026, 'Quest', [10,20,30,40], (100,200,300))
# print(t1)


# t1 = (10,20,30,40,50,60)

# print(t1[::-1])

# print(t1[-5:-1])


# t1 = (10,20,30,40,50)

# converted = list(t1)

# print(converted)

# converted.pop()

# print(converted)

# t1 = tuple(converted)
# print(t1)


# t2 = (60,70,80)

# result = t1 * 3

# print(result)

# print(id(t1))

# t1 += [60,70,80,90]
# print(id(t1))
# print(t1)




# fruits = ['apple','mango','banana','grape']

# """list unpacking"""

# item1, item2, *item3 = fruits

# print(item1)
# print(item2)
# print(item3)

# print(fruits)


# t1 = (10,20,30)

# t1 = (*t1,40,50)
# print(t1)

# t1 += (40,50)

# del t1

# print(t1)

# t1 = (10,20,30,40,30,10,20,30,30)

# print(t1.count(30))


# print(t1.index(100,3,-1))




# t1 = (10,20,30,40,50)

# for i in range(len(t1)):
#     print(t1[i])




# for i in range(11):
#     print(i)


# sentence = "My name is sreeraj"


# for i in sentence:
#     print(i)


# print(len(sentence))

# for i in range(len(sentence)):
#     print(sentence[i])


# length = 0

# for s in sentence:
#     length += 1

# print(length)
# print(len(sentence))
    


# i = 0

# while i <= 5:
#     print(i)
#     i += 1


# sample_set = {1,2,3,4,'Kochi',5,6,1,2,3,4,5,6,'Quest'}

# print(sample_set)

# for items in sample_set:
#     print(items)

# print(sample_set[0])

# empty_set = { }

# print(type(empty_set))

# empty_set1 = set()
# print(type(empty_set1))


# sample_set = {2026,2026, 'Quest', 1, True, False, 0, (5,26,'test'), {20,25,30}}
# print(sample_set)

# """false values = 0 False '' [] {} """


# list1 = [20,25,8,9,20,1,0,True, False]

# set1 = set(list1)

# print(set1)


# s1 = {1,2,3,4}

# s2 = {4,5,6,7}

# s1.clear()

# s1.pop()

# s1.pop()

# s1.discard(100)

# s1.remove(100)

# s1.update(s2)

# s1.add((20,25))

# print(s1)




# s1 = {1,2,3,4}

# s2 = {3,4,5,6,7}

# s4 = {10,20,30,40}


# s1 &=  s2
# print(s1)


"""symmetric difference"""

# result = s1.symmetric_difference(s2)
# result = s1 ^ s2
# print(result)

# s = s1.symmetric_difference_update(s2)
# print(s)


"""difference"""

# s2.difference_update(s1)

# print(s2)






"""intersection"""

# s2.intersection_update(s1)
# print(s2)

# intersection_set = s1 & s2

# intersection_set = s1.intersection(s2)

# print(intersection_set)


"""union"""

# s3 = s1 | s2 | s4

# # s3 = s1.union(s2,s4)
# print(s3)





# super_set = {1,2,3,4,5,6,7,8,9}

# sub_set1 = {100,200}

# print(sub_set1.issubset(super_set))

# print(super_set.issuperset(sub_set1))

# print(sub_set1.isdisjoint(super_set))



"""nexted dict"""

# student = {
#     # "name": "amjith",
#     # "age":25,
#     "address" : {
#         "place" : "kochi",
#         "district":"ernklm",
#         "state":"kerala"
#     }
# }


# for k, v in student.items():
#     print(k,v)

#     for addr, value in v.items():
#         print(addr,value)






# print(student["name"])
# print(student["age"])
# print(student["address"])
# print(student["address"]["district"])
# print(student["address"]["state"])

# student["address"]["pincode"] = 686514

# print(student["address"])


# student = {

#     "name" : "sreeraj",

#     "marks" : {
#         "python" : 85,
#         "django": 70,
#         "sql":95
#     },

#     "vismaya":{
#         "python":80,
#         "django":98,
#         "sql":80
#     }
# }

# for key, value in student.items():
#     print(key,"-", value)

#     for subject, mark in value.items():
#         print(subject, "-", mark)



# numbers = {}

# for i in range(1,6):
#     numbers[i] = i**2

# print(numbers)

# squares = { i : i**2 for i in range(1,6)}

# print(squares)


# names = ['sreeraj','vismaya','amjith','alisha']

# name_lengths = { i : len(i) for i in names }

# print(name_lengths)


# even_squares = { i:i**2 for i in range(1,11) if i % 2 == 0}

# print(even_squares)


# numbers = [12,2,5,6,7,8,96,4,5,1,23,65,45,78]

# even_odd = { n : "even" if n%2==0 else "odd" for n in numbers}

# print(even_odd)


# names = ["amjith",'vismaya','sreeraj','alisha']

# marks = [90,95,80,100]

# students = zip(names,marks)
# # print(dict(students))

# marks = dict(students)

# print(marks)




# x = int(input("Enter first number:"))

# y = int(input("Enter second number:"))

# print(x + y)


# for i in range(10):
#     print(i)


# if user == "login":


"""Functions"""

# def greet():
#     print("Welcome to Python functions")

# # function call

# greet()


# greet()


# def total():
#     x = 25
#     y = 20
#     result = x + y
#     print(result)

# total()


# def greet(name, email): #parameter
#     print(f"Welcome {name}!.Please verify your email: {email}")


# greet("Alisha", "alisha@gmail.com") #arguments

# greet("Alan","alan@gmail.com")


# def add(num1, num2):
#     print(f"Sum = {num1 + num2}")


# def substract(num1,num2):
#     print(f"Result = {num1 - num2}")




# x = int(input("Enter first number:"))
# y = int(input("Enter second number:"))
# add(x , y)

# substract(x, y)




# def to_upper(s : str)-> str: # type hinting
#     """this function accepts a string and return upper case format.
#     this is doc string
#     """
#     print(s.upper())

# to_upper("sree")


# def get_detailes(name:str = "unknown User", age:int = None) -> None:
#     print(f"Name : {name}\nAge : {age}")

# get_detailes("Alan",25)



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



# def add(num1 : int, num2 : int,num3 :int)->None:
#     print(f"Sum= {num1 + num2 + num3}")

# add(25,30,10)


# def add(*numbers):
#     total = 0
#     for i in numbers:
#         total += i
#     print(total)


# add(20,30)
# add(10)
# add(10,20,30,40,50)



# def student_details(**kwargs):
#     print(f"Name : { kwargs['name']}")
#     print(f"Age : {kwargs['age']}")
#     print(f"Place : {kwargs['place']}")

# # student_details(name = "Alan",course = "python", age = 22)
# student_details(place = "Kottayam")


# def student(*args, **kwargs):
#     print("postional arguments :",args)
#     print("Keyword Arguments :",kwargs)


# student(2026, "Sree", age = 24, place = "Kottayam")



# def add(a , b):
#     if a % 2 == 0:
#         return "even"
#     else:
#         return "odd"


# print(add(20,30))
# result = add(20,30)

# print(result)





"""Local and global scope"""

# x = 10
# def test():
#     global x
#     x = 20
#     print(x)

# test()
# print(x)



# count = 0

# def increase():
#     global count
#     count += 1

# increase()
# increase()
# increase()
# increase()
# increase()
# increase()
# print(count)




# def add_element(l : list) ->list:
#     l.append(100)


# sample = [10,20,30]
# add_element(sample)
# print(sample)


# def modify(a):
    

# a = [10,20,30]
# modify(a)
# print(a)



# def countdown(n):

#     if n == 0: # base condition
#         return

#     print(n)
#     countdown(n-1) # recursive

# countdown(3)



def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(5)) # 5*4*3*2*1