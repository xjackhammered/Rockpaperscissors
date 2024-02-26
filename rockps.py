from random import choice

def main():
    computer_choice = choice(["Rock","Paper","Scissors"])
    user_choice(computer_choice)

def user_choice(computer_choice):
    while True:
        try:
            user_choice = input("Rock, Paper or scissors? ").capitalize()
            if user_choice == "Exit":
                break
            else:
                computer(user_choice, computer_choice)

        except ValueError:
            pass

def computer(x, y):
    
    if x == "Paper" and y == "Rock":
        print("You chose " + x)
        print("Computer chose " + y)
        print("You win!")
    
    elif x == "Paper" and y == "Paper":
        print("You chose " + x)
        print("Computer chose " + y)
        print("It's a draw!")
    
    elif x == "Paper" and y == "Scissors":
        print("You chose " + x)
        print("Computer chose " + y)
        print("You lose!")
    
    elif x == "Scissors" and y == "Rock":
        print("You chose " + x)
        print("Computer chose " + y)
        print("You lose!")
    
    elif x == "Scissors" and y == "Scissors":
        print("You chose " + x)
        print("Computer chose " + y)
        print("It's a draw!")
    
    elif x == "Scissors" and y == "Paper":
        print("You chose " + x)
        print("Computer chose " + y)
        print("You win!")
    
    elif x == "Rock" and y == "Rock":
        print("You chose " + x)
        print("Computer chose " + y)
        print("It's a draw!")
    
    elif x == "Rock" and y == "Paper":
        print("You chose " + x)
        print("Computer chose " + y)
        print("You lose!")
    
    elif x == "Rock" and y == "Scissors":
        print("You chose " + x)
        print("Computer chose " + y)
        print("You win!")
    
    else:
        print("You chose " + x)
        print("Computer chose " + y)
        print("Not a valid choice.")

main()
    