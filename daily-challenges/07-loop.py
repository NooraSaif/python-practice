"""
challenge-1

Write a program that:

Takes two numbers as input
Iterates through the range of numbers from the first input to the second input (not including the second number)
Find and print the first even number greater than 5
Then, in a separate loop, find and print the first number divisible by 7
Output the result in the following format:
First even number greater than 5: ...
First number divisible by 7: ...

"""
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

for i in range(num1, num2):
  if i % 2 == 0 and i > 5:
    print(f"First even number greater than 5: {i}")
    break

for i in range(num1, num2):
  if i % 7 == 0:
    print(f"First number divisible by 7: {i}")
    break

"""
challenge-2-factorial

Write a program that calculates the factorial of a given integer.
Important: Your program should handle all non-negative integers, including 0 and 1.
How to approach this problem:

Read an integer input using int(input())
Initialize a result variable to 1 (since multiplying by 1 doesn't change the result)
Use a loop to multiply all numbers from 1 to the input number
Print the final result (just the number, no extra text)
"""
n = int(input())
result = 1
for i in range(1, n + 1):
    result *= i
print(result)

"""
challenge-3

Write a program that prints all odd numbers from 1 to 10 (inclusive) using a loop.
Then, in a separate loop, print all numbers from 10 down to 6 (inclusive) in descending order.

"""

for i in range(1, 11, 2):
  print(i)

for i in range(10, 5, -1):
  print(i) # result is 10, 9, 8, 7, 6 and 6 is included becuse 6 > 5

"""
challenge-4 dynamic input
Write a program that gets a dynamic number of input values.
The first input tells you how many numbers will follow. The next inputs are whole numbers that you need to sum.
In the end, print the sum of all the input numbers (not including the first input).
"""
n = int(input())
result = 0

for i in range(n):
    a = int(input())
    result += a
print(result)

"""
challenge-5 nested loop

"""
rows = 3
cols = 2

# Outer loop
for i in range(rows):
    print(f"Outer loop iteration: {i}")
    
    # Inner loop
    for j in range(cols):
        print(f"  Inner loop iteration: {j}")

"""
challenge-6 
Write a program that counts the number of even numbers between 10 and 50 (inclusive).
Use a for loop and an if statement to check if each number is even and count how many even numbers there are.
Store the count in a variable called count_even.
"""
count_even = 0
for i in range(10, 51):
    if i % 2 == 0:
        count_even += 1
print(count_even)

"""
challenge-7
Create a program that performs the following tasks using range():
task-1: Print all numbers from 30 to 80 (inclusive) that are divisible by 4
task-2: Print the first 8 odd numbers starting from 15
task-3: Count backwards from 50 to 10 (inclusive), showing only numbers divisible by 5
task-4: Calculate and print the product of all numbers from 1 to 30 (inclusive) that are divisible by 3
"""
# Task 1: Numbers divisible by 4 between 30-80
print("Numbers divisible by 4 between 30-80:")
for num in range(30, 81):
    if num % 4 == 0:
        print(num, end=", ")
print()  # new line

# Task 2: First 8 odd numbers from 15
print("\nFirst 8 odd numbers from 15:")
for num in range(15, 30, 2):  # 15 to 29 stepping by 2
    print(num, end=", ")
print()

# Task 3: Counting backwards, divisible by 5
print("\nCounting backwards, divisible by 5:")
for num in range(50, 9, -5):  # 50 to 10 stepping by -5
    print(num, end=", ")
print()

# Task 4: Product of numbers divisible by 3
print("\nProduct of numbers divisible by 3 (1-30):")
product = 1
for num in range(3, 31, 3):  # stepping by 3 directly
    product *= num
print(product)

""" 
challenge-8
Write a program that finds all pairs of numbers that multiply to give n using numbers from 1 to n (inclusive).
The program should show all possible combinations, including duplicate pairs in reverse order. For example, both "1 6" and "6 1" should be shown, as they are considered different arrangements of the same pair. Numbers can also be paired with themselves if their product equals n.

Important: Only consider numbers in the range from 1 to n. If n is less than 1, no pairs exist.
"""
n = 12
for i in range(1, n+1):
    for j in range(1, n+1):
        if i * j == n:
            print(i, j)
# result:
# 1 12
# 2 6
# 3 4
# 4 3
# 6 2
# 12 1
