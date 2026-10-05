# print and input
# variables
# data type
# list, tuple, set
# string operations
# operations

user_name = 'Joha'
phone_number = 9876543

print("it's python course")
print('it\'s')
print("1- your name is", user_name)
print("2- your name is " + user_name) # Works only if the variable is a string
print(f"1- your name is {user_name}") # the best to use

# Convert data type
num1 = str(20)
print(type(num1))

num2 = int(3.8)
num3 = float(2)
print(num2, num3)

# list, tuple, set
fineds_lists = ['John','Michael','Terry','Eric','Graham','Eric']
frinds_tuple = ('John','Michael','Terry','Eric','Graham','Eric')
frinds_set = {'John','Michael','Terry','Eric','Graham','Eric'}

# -----------------------list---------------------------------
print(fineds_lists[0])
print(fineds_lists[2:4])
print(fineds_lists[-1])
print(fineds_lists[:2])
print(fineds_lists[2:])

# len, index, count
print(fineds_lists.index('John')) # 0
print(fineds_lists.count('John')) # كم مره تكرر 1
print(len(fineds_lists)) # عدد العناصر في القائمه 6

# sort, reverse, [::-1]
fineds_lists.sort()
fineds_lists.sort(reverse=True)
fineds_lists.sort(key=len) # ترتيب على حسب الطول
fineds_lists.reverse() # عكس القائمه بدون ترتيب
fineds_lists[::-1]
print(fineds_lists)
for n in reversed([1, 2, 3, 4,]):
  print(n)


# extend, append, insert to add element
print(fineds_lists.append('Noora')) #add item to the end
print(fineds_lists.insert(1, 'Noora')) # insert item at specific index
print(fineds_lists.extend(["Nada", "Noora"])) # add another list

# remove, pop
fineds_lists.remove("Eric")
print(fineds_lists) # remove the first Eric
print(fineds_lists.pop()) #remove and return the last item
print(fineds_lists)

if "John" in fineds_lists:
  fineds_lists.remove("John")
  print(fineds_lists)
else:
  print("Not available")

del fineds_lists[1] # to delete based on index
print(fineds_lists)


# -----------------------Tuple-------------------------
# hashable, immutable, ordered, allows duplicates
# .add() .remove() .update() .discard() .pop() 
# .union() .intersection() .difference() .symmetric_difference()
empty = tuple()






# ------------------------set----------------------------
# no duplicates, fast checking
empty = set()