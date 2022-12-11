print("Welcom to my Quiz Game!") 
play = input("Do you want to play? ")

if play.lower() != "yes":
    quit()
else:
    print("Okay! Let's do this")
score = 0

answer = input("what does CPU stand for?\n")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect')
# You can add more quiz below

# Printing your scores
print(f"You got {score} points")
