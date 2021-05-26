winning_number = 69
user_input = int(input("Guess the number between 1 to 100 "))
if user_input == winning_number :
    print("YOU WIN !!!")
else :
    if user_input < winning_number :
        print("too low")
    else :
        print("too high")
