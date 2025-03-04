#snake , water ang gun game
import random

def game():

    choices = ["snake","gun","water"]
    #random computer choice
    computer_choice = random.choice(choices)
    #user choice in that set only
    user= input("enter the choice(snake, gun, water) : ").lower()

    if user not in choices:
        print("invalid choice!. Enter the valid choice ")
        return
    
    print(f"computer choice is {computer_choice}\ user choice is {user}")

    if(computer_choice == user):
        print("Its a tie!")

    elif(user == "snake" and computer_choice == "water") or \
         (user == "water" and computer_choice == "gun") or \
         (user == "gun" and computer_choice == "snake"):
        print("You win!")

    else:
        print("You loose!")   

#run the game
game()        
 