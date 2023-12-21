print("Welcome to my animal quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play! :)")
score = 0

answer = input("What animal has the thickest fur of any mammal? ")
if answer.lower() == "sea otter":
    print("Correct!")
    score += 1
else:
    print("Sorry, that's not correct.")

answer = input("What is a group of cats called? ")
if answer.lower() == "clowder":
    print("Correct!")
    score += 1
else:
    print("Sorry, that's not correct.")

answer = input("What body part is used to determine the age of a lion? ")
if answer.lower() == "nose":
    print("Correct!")
    score += 1
else:
    print("Sorry, that's not correct.")

answer = input("What is the only mammal capable of true flight? ")
if answer.lower() == "bat":
    print("Correct!")
    score += 1
else:
    print("Sorry, that's not correct.")

answer = input("What is a baby hedgehog called? ")
if answer.lower() == "hoglet":
    print("Correct!")
    score += 1
else:
    print("Sorry, that's not correct.")

print("Congratulations! You got " + str(score) + " questions correct!")