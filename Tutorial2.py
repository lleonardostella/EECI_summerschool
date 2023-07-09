# Tutorial 2: Conditionals and Loops

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

# Congratulations on completing the second tutorial!

