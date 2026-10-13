# if statment
"""
challeng-1:
Your task is to initialize variable status based on the conditions:

"Calm" if wind is smaller than 8,
"Breeze" if wind is between 8 and 31 (including 8 and 31).
"Gale" if wind is between 32 and 63 (including 32 and 63)
"Storm" otherwise

"""
wind = 12
status = "unset"
# Type your code below
if wind < 8:
    status = "Calm"
elif wind >= 8 and wind <=31:
    status = "Breeze"
elif wind >= 32 and wind <= 63:
    status = "Gale"
else:
    status = "Storm"

# Don't change the line below
print(f"status = {status}")


"""
challeng-2
The possible values for op are '+', '-', '/' and '*'

Your task is to set the variable result based on the conditions:

if op is '+', set result with n1 + n2.
if op is '-', set result with n1 - n2.
if op is '/', set result with n1 / n2.
if op is '*', set result with n1 * n2.
"""

n1 = 1 
n2 = 2
op = "+"
result = 0

if op == "+":
    result = n1 + n2
if op == "-":
    result = n1 - n2
if op == "/":
    result = n1 / n2
if op == "*":
    result = n1 * n2
    
# Don't change the line below
print(f"result = {result}")