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

# 1️⃣ List (JS array jaisa)////////////////////////////

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

# 1️⃣ List (JS array jaisa)////////////////////////////

# 2️⃣ Tuple (Immutable list)//////////////////////

# coordinates = (10, 20, 30)

# print(coordinates[0])
# print(coordinates[1])
# print(coordinates[2])


# 2️⃣ Tuple (Immutable list)//////////////////////

# 3️⃣ Set (Unique values only)/////////////////

# nums = {1, 2, 3, 3, 4}
# print(nums)   # {1, 2, 3, 4}

# nums.add(5)     # naya element add karna 
# print(nums)
# nums.remove(2)   # ek element hatana
# print(nums)


# 3️⃣ Set (Unique values only)/////////////////

# 4️⃣ Dictionary (JS object jaisa)///////////////

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

# 4️⃣ Dictionary (JS object jaisa)///////////////

# 5️⃣ List Comprehension (Shortcut for loops)

# squares = [x**2 for x in range(1, 6)]
# print(squares)  # [1, 4, 9, 16, 25]


# 5️⃣ List Comprehension (Shortcut for loops)

# 6️⃣ File Handling (Read/Write file)/////////////////

# Write
# with open("data.txt", "w") as f:
#     f.write("Hello Python File!")

# # Read
# with open("data.txt", "r") as f:
#     content = f.read()
#     print(content)


# 6️⃣ File Handling (Read/Write file)/////////////////

# 7️⃣ OOP (Classes & Objects)

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def drive(self):
#         print(f"{self.brand} {self.model} is driving 🚗")

# car1 = Car("Toyota", "Corolla")
# car1.drive()

# 7️⃣ OOP (Classes & Objects)

# 🐍 Step 2: Python Data Structures

