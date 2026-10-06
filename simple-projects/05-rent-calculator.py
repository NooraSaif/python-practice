# claculate the cost of each person in the room
"""
Input:
- enter room rent
- enter wifi
- enter total electricity spend 
- enter total water spend
- enter total gas spend
- enter number of people in the room 

Output:
- the cost of each person in the room:

"""

rent = float(input("Enter room rent: "))
wifi = float(input("Enter wifi cost: "))
electricity = float(input("Enter total electricity spend: ") )
water = float(input("Enter total water spend: "))
gas = float(input("Enter total gas spend: "))
number_of_people = int(input("Enter number of people in the room: "))

result = (rent + wifi + electricity + water + gas) / number_of_people

print ("The cost of each person in the room is: ", result)
