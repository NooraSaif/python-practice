"""
challenge-1
Write a program that receives a number n as input() and executes the function hello_function() n times
"""
def hello_function():
    print("Hello Function!")

n = int(input())
for i in range(n):
    hello_function()

"""
challenge-2 arguments/parameters
Create a program that calculates the area of a rectangle. The program should take two inputs: the length and width of the rectangle.

Define a function that accepts two arguments (length and width), calculates the area of the rectangle (length * width), and prints the result.

After defining the function, prompt the user for the length and width inputs, and then call your function with these inputs.
"""
def calculate_area(length, width):
    area = length * width
    print(area)

length = float(input())
width = float(input())
# Call the function 
calculate_area(length, width)

"""
challenge-3 return
Create a function called square_number that takes a single parameter n and returns its square (n × n).
Create a variable called input_num that takes input from the user (convert it to int using int()).
Call the function with input_num as the argument, and store the returned value in a variable called result.
Finally, print result.
"""
def square_number(n):
    return n * n

input_num = int(input())
result = square_number(input_num) #the result variable will hold n*n value because this is what the function returned.
print(result)