print("Welcome to my animal quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's play! :)")

answer = input("What mammal has the thickest fur of any mammal?")
if answer == "sea otter":
    print("Correct!")
else:
    print("Sorry, that's not correct.")

answer = input("What is a group of cats called?")
if answer == "clowder":
    print("Correct!")
else:
    print("Sorry, that's not correct.")

answer = input("What body part is used to determine the age of a lion?")
if answer == "nose":
    print("Correct!")
else:
    print("Sorry, that's not correct.")

answer = input("What is the only mammal capable of true flight?")
if answer == "bat":
    print("Correct!")
else:
    print("Sorry, that's not correct.")

answer = input("What is a baby hedgehog called?")
if answer == "hoglet":
    print("Correct!")
else:
    print("Sorry, that's not correct.")