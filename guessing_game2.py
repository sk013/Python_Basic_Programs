import random

number = int(input("Guess the number between 1 to 100 "))
winning_number = random.randint(1,100)
guess = 1
while True :
    if winning_number == number :
        print(f"You Win!!!...And you guessed the number in {guess} times ")
        if guess>5 :
            print("you attempted too many times IDIOT!!!")
        break
    else :
        if number > winning_number :
            print("Too high ")
        else :
            print("Too low ")
        guess += 1
        number = int(input("Guess again "))