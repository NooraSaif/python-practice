# Logical Operators (and, or, not)
# comparison operations == != < > <= >=  
"""
chelleng:
Write code that checks if a person is eligible to drive. A person is eligible if ALL of the following are true:

The person is at least 18 years old
The person has a license
The person has insurance

"""
age = int(input("Enter your age: "))
has_license = input("do you have a license (false/true): ").lower() == "true"
has_insurance = input("do you have insurance (false/true):").lower() == "true"

result = age >= 18 and has_license and has_insurance 

print(result)