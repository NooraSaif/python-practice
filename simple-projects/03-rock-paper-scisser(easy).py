import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scisser"]
# options[0] = rock 

while True:
  user_input = input("Choose rock/paper/scisser or q to quit: ").lower()

  if user_input == "q":
    break

  if user_input not in options:
    print("invalid input please try agin")
    continue

  randomChoice = random.randint(0,2)
  # rock=0 , paper=1 , scisser=2 index from the list
  computer_pick = options[randomChoice]

  if user_input == "rock" and computer_pick == "scisser":
    print("you win")
    user_wins +=1
  elif user_input == "scisser" and computer_pick == "paper":
      print("you win")
      user_wins +=1
  elif user_input == "paper" and computer_pick == "rock":
      print("you win")
      user_wins +=1
  elif user_input == computer_pick:
      print("Tie")
  else:
      print("you loss")
      computer_wins +=1

  print("you picked: ", user_input)
  print ("computer picked: ", computer_pick)
  print (f"wins: {user_wins} loss: {computer_wins}")
print("Goodbay!")


