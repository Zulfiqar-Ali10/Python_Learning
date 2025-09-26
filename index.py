# ///////////////// Hello Print //////////////////////

# print("Hello, World")

# ///////////////// Hello Print //////////////////////

# ///////////////// Ask Name //////////////////////

# name = input("Enter your name?")
# print(f"Hello {name}, welcome!")

# ///////////////// Ask Name //////////////////////

# /////////////////1️⃣ Variables & Data Types//////////////////////

# name = "Zulfiqar"
# print(name)
# print(name[3])


# age = 20
# print(age)
# print(age + 10)


# pi = 3.14
# print(pi)

# is_student = True
# print(is_student)

# print(name, age, pi, is_student)

# /////////////////1️⃣ Variables & Data Types//////////////////////


# ////////////////2️⃣ Operators ////////////////////

# a = 10
# b = 3

# print(a + b)
# print(a - b) 
# print(a * b)
# print(a / b) 
# print(a // b)
# print(a % b)  
# print(a ** b)

# ////////////////2️⃣ Operators ////////////////////

# 3️⃣ Conditions (if, elif, else) //////////////////

# num = int(input("Enter a number:"))

# if num > 0:
#     print("Positive number")
# elif num < 0:
#         print("Negative number")
# else:
#             print("Zero")


# age = int(input("Enter your age:"))

# if age >= 18:
#     print("You are an Adult")
# elif age >= 13:
#     print("You are a Teenager")
# else:
#     print("You are a Child")

# 3️⃣ Conditions (if, elif, else) //////////////////


# 4️⃣ Loops (for & while) ///////////////////////

# for loop

# for i in range(5):
#     print("Hello", i)


# while loop

# x = 0
# while x < 5:
#     print("Hello", x)
#     x += 1


# x =  0
# while x <= 10:
#     print("Number:", x)
#     x += 1

# 4️⃣ Loops (for & while) ///////////////////////

# 5️⃣ Functions (def)//////////////////////

# def greet(name):
#  return f"Hello {name}, Welcome to Python!"

# print(greet("Zulfiqar"))

# def add(a, b):
#     return a + b
# print(add(10, 20))

# 5️⃣ Functions (def)//////////////////////


# 6️⃣ Error Handling (try/except) /////////////

# try:
#     num = int(input("Enter a number: "))
#     print("Square:", num ** 2)
# except ValueError:
#     print("Invalid input! Please enter a valid number.")

# try:
#     age =  int(input("Enter a number:"))
#     print("Divided by 2", age / 2)
# except ValueError:
#     print("Invalid input! Please enter a valid number.")

# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))

#     result = num1 / num2
#     print("Result:", result)

# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("Invalid input! Please enter valid numbers.")

# 6️⃣ Error Handling (try/except) /////////////

# 🐍 Step 2: Python Data Structures

# 7 List (JS array jaisa)////////////////////////////

# fruits = ["apple", "banana", "mango"]

# print(fruits[1])
# fruits.append("orange")
# fruits.remove("banana")
# print(fruits)

# for f in fruits:
#     print(f)


# numbers = [1, 2, 3, 4, 5]

# print("Sum:", sum(numbers))
# print("Max:", max(numbers))
# print("Min:", min(numbers))

# 7 List (JS array jaisa)////////////////////////////

# 8 Tuple (Immutable list)//////////////////////

# coordinates = (10, 20, 30, 20)

# print(coordinates[0])
# print(coordinates[1])
# print(coordinates[2])
# print(coordinates)   


# 8 Tuple (Immutable list)//////////////////////

# 9 Set (Unique values only)/////////////////

# nums = {1, 2, 3, 3, 4}
# print(nums)   # {1, 2, 3, 4}

# nums.add(5)     # naya element add karna 
# print(nums)
# nums.remove(2)   # ek element hatana
# print(nums)


# 9 Set (Unique values only)/////////////////

# 10 Dictionary (JS object jaisa)///////////////

# student = {
#     "name": "Ali",
#     "age": 22,
#     "city": "Lahore"
# }

# # print(student["name"])   # Ali
# student["age"] = 23      # update
# student["country"] = "Pakistan"  # new key
# # print(student)
# for key, value in student.items():
#     print(key, ":", value)

# 10 Dictionary (JS object jaisa)///////////////

# 11 List Comprehension (Shortcut for loops)

# squares = [x**2 for x in range(1, 6)]
# print(squares)  # [1, 4, 9, 16, 25]

# evens = [x for x in range(10) if x % 2 == 0]
# print(evens)  
# # [0, 2, 4, 6, 8]

# labels = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 6)]
# print(labels)
# # ['Odd', 'Even', 'Odd', 'Even', 'Odd']



# 11 List Comprehension (Shortcut for loops)

# 12 File Handling (Read/Write file)/////////////////

# Write
# with open("data.txt", "w") as f:
#     f.write("Hello Python File!")

# # Read
# with open("data.txt", "r") as f:
#     content = f.read()
#     print(content)


# 12 File Handling (Read/Write file)/////////////////

# 13 OOP (Classes & Objects)

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def drive(self):
#         print(f"{self.brand} {self.model} is driving 🚗")

# car1 = Car("Toyota", "Corolla")
# car1.drive()

# 13 OOP (Classes & Objects)

# 🐍 Step 2: Python Data Structures


# 🐍 Python Intermediate Concepts//////////////////////

#Lambda 14 //////////////////////////////////////
#normal function
# def add(a, b):
#     return a + b
# print(add(2, 3))

#Lambda function Shortcut for small functions

# add = lambda a, b: a + b
# print(add(10, 20))

# sort a list of tuples by second value

# pairs = [(1, 10), (2, 5), (3, 7)]
# pairs.sort(key=lambda x: x[1])
# print("Sort Pairs", pairs)

#Lambda function Shortcut for small functions

#Lambda 14 //////////////////////////////////////

# 15 Map, Filter, Reduce ////////////////////////

# numbers = [1, 2, 3, 4, 5]

# Map 
# squares = list(map(lambda x: x**2, numbers))
# print("Squares:", squares)

# Filter 
# numbers = [1, 2, 3, 4, 5]
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# print("Evens:", evens)

# Reduce 
# from functools import reduce

# numbers = [1, 2, 3, 4, 5]
# product = reduce(lambda a, b: a * b, numbers )

# print("Product:", product)


# users = [
#     {"name": "Ali", "age": 20},
#     {"name": "Sara", "age": 25},
#     {"name": "Ahmed", "age": 30}
# ]

# # extract only names (map)
# names = list(map(lambda u: u["name"], users))

# # filter adults (age >= 25)
# adults = list(filter(lambda u: u["age"] >= 25, users))

# print(names)   # ['Ali', 'Sara', 'Ahmed']
# print(adults)  # [{'name': 'Sara', 'age': 25}, {'name': 'Ahmed', 'age': 30}]

# 15 Map, Filter, Reduce ////////////////////////


# 16 Iterators & Generators//////////////////////////

# nums = [1, 2, 3]
# it = iter(nums)

# print(next(it))
# print(next(it))
# print(next(it))


# def generate_numbers(n):
#     for i in range(1, n+1):
#         yield i  # generator returns one item at a time

# gen = generate_numbers(5)
# for num in gen:
#     print(num)


# 16 Iterators & Generators//////////////////////////


# 17 Decorators////////////////////////////////////

# def decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper

# @decorator
# def say_hello():
#     print("Hello!")

# say_hello()


# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"Execution time: {end - start:.4f} seconds")
#         return result
#     return wrapper

# @timer
# def slow_function():
#     time.sleep(2)
#     print("Done!")

# slow_function()


# 17 Decorators////////////////////////////////////


# 18 Context Managers (with open)//////////////////////

# with open("test.txt", "w") as f:
#     f.write("Hello Context Manager!")



# class CustomContext:
#     def __enter__(self):
#         print("Enter block")
#         return "Resource Ready"

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Exit block")

# with CustomContext() as res:
#     print(res)


# 18 Context Managers (with open)//////////////////////


# 19 Regular Expressions (regex)///////////////////

# import re

# text = "My number is 0300-1234567"
# pattern = r"\d{4}-\d{7}"
# match = re.search(pattern, text)

# if match:
#     print("Number found:", match.group())


# emails = ["test@gmail.com", "invalid@", "user@yahoo.com"]

# valid_emails = [e for e in emails if re.match(r"[^@]+@[^@]+\.[^@]+", e)]
# print(valid_emails)  # ['test@gmail.com', 'user@yahoo.com']


# 19 Regular Expressions (regex)///////////////////



# 20 JSON Handling/////////////////////////////////

# import json

# user = {"name": "Ali", "age": 25}

# # dict → JSON
# json_str = json.dumps(user)

# # JSON → dict
# parsed = json.loads(json_str)

# print(json_str)  # {"name": "Ali", "age": 25}
# print(parsed["name"])  # Ali


# data = '''
# [
#   {"name": "Ali", "age": 20},
#   {"name": "Sara", "age": 25}
# ]
# '''

# users = json.loads(data)
# for u in users:
#     print(u["name"], u["age"])



# 20 JSON Handling/////////////////////////////////


# 21 Datetime Module/////////////////////////////////

# from datetime import datetime

# now = datetime.now()
# print(now)
# print(now.strftime("%Y-%m-%d %H:%M:%S"))


# from datetime import datetime, timedelta

# today = datetime.today()
# future = today + timedelta(days=7)

# print("Today:", today.strftime("%Y-%m-%d"))
# print("After 7 days:", future.strftime("%Y-%m-%d"))


# 21 Datetime Module/////////////////////////////////


# 🐍 Python Intermediate Concepts//////////////////////

