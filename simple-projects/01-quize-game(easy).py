answer = input("Do you want to paly? (yes/no) ")
if answer.lower() == "yes":
    print("Great! Let's start the quiz.")
else:
    print("No worries! Maybe next time.")
    quit()

score = 0

answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Paris.")

answer = input("What is 5 + 7? ")
if answer == "12":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 12.")

print("Your final score is: " + str(score) + "/2")
print(f"Your present is: {score/2 * 100}%")


