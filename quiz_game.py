class answers:
    first = "sea otter"
    second = "clowder"
    third = "nose"
    fourth = "bat"
    fifth = "hoglet"
obj = answers()

print("Welcome to my animal quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play! :)")
score = 0
print("Current Score: ", score)

answer = input("What animal has the thickest fur of any mammal? ")
if answer.lower() == answers.first:
    print("Correct!")
    score += 1
    print("Current Score: ", score)
else:
    print("Sorry, the correct answer is: ", answers.first)
    print("Current Score: ", score)
answer = input("What is a group of cats called? ")
if answer.lower() == answers.second:
    print("Correct!")
    score += 1
    print("Current Score: ", score)
else:
    print("Sorry, the correct answer is: ", answers.second)
    print("Current Score: ", score)
answer = input("What body part is used to determine the age of a lion? ")
if answer.lower() == answers.third:
    print("Correct!")
    score += 1
    print("Current Score: ", score)
else:
    print("Sorry, the correct answer is: ", answers.third)
    print("Current Score: ", score)
answer = input("What is the only mammal capable of true flight? ")
if answer.lower() == answers.fourth:
    print("Correct!")
    score += 1
    print("Current Score: ", score)
else:
    print("Sorry, the correct answer is: ", answers.fourth )
    print("Current Score: ", score)
answer = input("What is a baby hedgehog called? ")
if answer.lower() == answers.fifth:
    print("Correct!")
    score += 1
    print("Final Score: ", score)
else:
    print("Sorry, the correct answer is: ", answers.fifth)
    print("Final Score: ", score)
print("Congratulations! You got " + str(score) + " questions correct!")
print("That's " + str(score/5 * 100) + "%!")

