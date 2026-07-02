import random

while True:
    a = random.randint(1,100)
    while True:
        
        try:
            guess = int(input("guess the number between 1 and 100: "))
            if guess < 1 or guess > 100:
                print("invalid number.")
            elif guess > a :
                print("Too high.")
            elif guess < a:
                print("Too low.")
            else:
                print("Conguratulations!")
                break
        except ValueError:
            print("please enter a valid value.")

    again = input("Would you like to play again? (yes/no): ").lower()
    
    if again == "yes":
        print("ok")
    elif again == "no":
        print("Thanks for playing!")
    else:
        print("Please enter only 'yes' or 'no'.")
        break
    
