# Logical Operators (and, or, not)
# comparison operations == != < > <= >=  
"""
chelleng-1:
Write code that checks if a person is eligible to drive. A person is eligible if ALL of the following are true:

The person is at least 18 years old
The person has a license
The person has insurance

"""
# age = int(input("Enter your age: "))
# has_license = input("do you have a license (false/true): ").lower() == "true"
# has_insurance = input("do you have insurance (false/true):").lower() == "true"

# result = age >= 18 and has_license and has_insurance 

# print(result)

"""
challenge-2:

You're helping a pet shop create a system to determine if they can sell a pet to a customer

Initialize the following variables:

has_license with the value True
has_space with the value True
has_experience with the value False

Write logical expressions to determine if:

can_sell_regular_pet: Customer can buy a regular pet if they have EITHER a license OR experience, AND they must have space
can_sell_exotic_pet: Customer can buy an exotic pet if they have BOTH a license AND experience, AND they must have space
cannot_sell_any_pet: The shop CANNOT sell any pet if the customer has NO license AND NO experience, OR they have NO space

Expected Results with the given values:

can_sell_regular_pet: True (has license and space)
can_sell_exotic_pet: False (no experience)
cannot_sell_any_pet: False (has both license and space)
"""

has_license = True
has_space = True
has_experience = False

can_sell_regular_pet = (has_license or has_experience) and has_space
print(can_sell_regular_pet)  # result: True

can_sell_exotic_pet = has_license and has_experience and has_space
print(can_sell_exotic_pet) # result: False

# cannot_sell_any_pet = has_license and has_experience and has_space
cannot_sell_any_pet = (not has_license and not has_experience) or not has_space
print(cannot_sell_any_pet) # result: False