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