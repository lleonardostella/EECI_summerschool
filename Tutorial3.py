# Tutorial 3: Functions, Lists, and File Handling

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

# Congratulations on completing all three tutorials!

