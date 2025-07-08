print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("Which is the longest river in the world? ")
if answer.lower() == " Nile River":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the chemical formula for water? ")
if answer.lower() == "H2O":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("Which country hosted the 2024 Summer Olympics? ")
if answer.lower() == "France":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does OS stand for? ")
if answer.lower() == "operating system":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does HDD stand for? ")
if answer.lower() == "hard disk drive":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")