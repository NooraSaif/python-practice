def add():
  account_name = input("Enter your account name: ")
  password = input("Enter new password: ")

  with open('password.txt', 'a') as f:
    f.write(account_name + '|' + password + '\n')

def view():
  with open('password.txt', 'r') as f:
    for line in f:
      print(line.rstrip())


while True:
  userInput = input("Would u like to Add or view password or enter q to quite: ").lower()
  if userInput == "q":
    break

  if userInput == "add":
    add()

  elif userInput == "view":
    view()

  else:
    print("Invalid input")
    continue

print("goodbay")