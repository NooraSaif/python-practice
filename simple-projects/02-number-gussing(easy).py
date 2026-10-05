import random

topRange = input("Enter Top Range: ")

if topRange.isdigit():
    topRange = int(topRange)

    if topRange <= 0:
      print("Please enter a number greater than 0 next time.")
      quit()

else:
    print("Please enter a number next time.")
    quit()

computerGuss = random.randint(0, topRange)
gussess = 0

while True:
  userGuess = input(f"Guess a number between 0 and {topRange}: ")

  if userGuess.isdigit():
      userGuess = int(userGuess)
  else:
      print("please enter a number next time")
      continue
  
  gussess += 1
  if userGuess == computerGuss:
    print(f"computer guss is {computerGuss}. You win")
    break
  elif userGuess < computerGuss:
    print("Too low!")
  else:
    print("Too high!")

print(f"you got it in, {gussess}, gusses" )