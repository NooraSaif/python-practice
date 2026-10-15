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

if wind < 8:
    status = "Calm"
elif wind >= 8 and wind <=31:
    status = "Breeze"
elif wind >= 32 and wind <= 63:
    status = "Gale"
else:
    status = "Storm"

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
    
print(f"result = {result}")

"""
challeng-3

Create a program for a game character creation system. The requirements are:

The character's level determines what weapons they can use:

Level 1-5: Can only use Basic weapons
Level 6-10: Can use Advanced weapons if they completed training
Level 11+: Can use any weapon
Set level_message variable with these messages based on the conditions:

If level 1-5: Basic weapons only
If level 6-10 and no training: Need weapon training first
If level 6-10 and has training: Access to advanced weapons granted
If level 11+: Access to all weapons granted
If level is 0 or negative: Invalid level

"""
level = int(input("enter number of the level: ")) 
has_training = True
level_message = "None" 

# Write your code below
if level >= 1 and level <=5:
    level_message = "Basic weapons only"
elif level >= 6 and level <= 10 and not(has_training):
    level_message = "Need weapon training first"
elif level >= 6 and level <= 10 and has_training:
    level_message = "Access to advanced weapons granted"
elif level >= 11:
    level_message = "Access to all weapons granted"
else:
    level_message = "Invalid level"

print(level_message)