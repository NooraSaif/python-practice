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


