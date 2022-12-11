print("Welcom to my Quiz Game!")

play = input("Do you want to play? ")

if play != "yes":
    quit()
else:
    print("Okay! Let's do this")

answer = input("what does CPU stand for?\n")
if answer == "central processing unit" or "Central Processing Unit":
    print('Correct!')
