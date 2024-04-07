# Tutorial 1 
# Part 1: Introduction to Python

# Printing "Hello World" to the console
print("Hello World!")

# Variables and Data Types
message = "Welcome to Python!"
print(message)

# Numbers
num1 = 10
num2 = 5
sum = num1 + num2
print("The sum of", num1, "and", num2, "is", sum)

# Strings
name = "John"
age = 25
print("My name is", name, "and I am", age, "years old.")

# User Input
name = input("Enter your name: ")
print("Hello,", name, "!")

# Basic Math Operations
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
product = num1 * num2
print("The product of", num1, "and", num2, "is", product)

# Comments
# This is a single-line comment
"""
This is a
multi-line comment
"""



# Part 2: Conditionals and Loops

# If-else Statements
age = 18
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Comparison Operators
num1 = 10
num2 = 5
if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 < num2:
    print(num1, "is less than", num2)
else:
    print(num1, "is equal to", num2)

# Logical Operators
is_raining = True
is_sunny = False
if is_raining and not is_sunny:
    print("It's raining.")
elif not is_raining and is_sunny:
    print("It's sunny.")
elif is_raining and is_sunny:
    print("It's both raining and sunny.")
else:
    print("It's neither raining nor sunny.")

# While Loop
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# For Loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I love", fruit + "s")

# Range Function
for num in range(1, 6):
    print(num)

# Break and Continue Statements
for num in range(1, 11):
    if num == 5:
        break  # Exit the loop
    if num % 2 == 0:
        continue  # Skip the current iteration
    print(num)


# Part 3: Functions, Lists, and File Handling

# Functions
def greet(name):
    print("Hello,", name + "!")

greet("Alice")
greet("Bob")

def add_numbers(num1, num2):
    return num1 + num2

result = add_numbers(10, 5)
print("The sum is:", result)

# Lists
fruits = ["apple", "banana", "cherry"]
print("First fruit:", fruits[0])
print("Number of fruits:", len(fruits))

fruits.append("durian")
print("Updated fruits list:", fruits)

for fruit in fruits:
    print("I have", fruit + "s")

# File Handling
file = open("data.txt", "w")
file.write("Hello, World!")
file.close()

file = open("data.txt", "r")
content = file.read()
print("File content:", content)
file.close()

# Error Handling
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")