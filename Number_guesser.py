import random

random_number = random.randint(1,10)
while True:
    guess = input("\nType a number: ")
    if guess.isdigit():
        guess = int(guess)

        if guess <= 0:
            print('Enter a positive number larger than 0 and not more than 10')
            quit()
    else:
        print('Enter a positive number larger than 0 and not more than 10')
        quit()

    if guess == random_number:
        print('You got it!')
        break
    else:
        if guess > random_number:
            print('You are above the number!\nTry again')
        else:
            print('You are below the number!\nTry again')

        


