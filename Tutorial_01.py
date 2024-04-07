# Tutorial 1 
# Part 1: Introduction to Python

# Printing to the console
print("Hello World! This is the first day of the EECI course on Game Theory with Engineering Applications")

# Variables and data types
message = "Welcome to Birmingham!"
print(message)

# Numbers
num1 = 30
num2 = 15
sum = num1 + num2
print("The sum of", num1, "and", num2, "is", sum)

# Strings
name = "Leonardo"
age = 33
print("My name is", name, "and I am", age, "years old.")

# User input
name = input("Enter your name: ")
print("Hello,", name, "!")

# Basic math operations
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


# If-else statements
age = 18
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Comparison operators
num1 = 1
num2 = 15
if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 < num2:
    print(num1, "is less than", num2)
else:
    print(num1, "is equal to", num2)

# Logical operators
is_raining = True
is_sunny = False
if is_raining and not is_sunny:
    print("It is raining.")
elif not is_raining and is_sunny:
    print("It is sunny.")
elif is_raining and is_sunny:
    print("It is raining and sunny at the same time.")
else:
    print("It is neither raining nor sunny.")

# Loops
# While loop
count = 1
while count <= 10:
    print("Count:", count)
    count += 1

# For loop
fruits = ["apple", "banana", "watermelon"]
for fruit in fruits:
    print("I love", fruit + "s")

# Range function
for num in range(1, 11):
    print(num)

# Break and Continue Statements
for num in range(1, 11):
    if num == 5:
        break  # Exit the loop
    if num % 2 == 0:
        continue  # Skip the current iteration
    print(num)


# Functions, lists and file handling

# Functions
def greet(name):
    print("Hello,", name + "!")

greet("Leonardo")
greet("Dario")

def add_numbers(num1, num2):
    return num1 + num2

result = add_numbers(12, 7)
print("The sum is:", result)

# lists
fruits = ["apple", "banana", "watermelon"]
print("First fruit:", fruits[0])
print("Number of fruits:", len(fruits))

fruits.append("durian")
print("Updated fruits list:", fruits)

for fruit in fruits:
    print("I have", fruit + "s")

# File handling
file = open("data.txt", "w")
file.write("Hello, World!")
file.close()

file = open("data.txt", "r")
content = file.read()
print("File content:", content)
file.close()

# Error handling
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")