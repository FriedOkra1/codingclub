import random

while(1):
    
    print("Whats your choice? 'r' for rock, 'p' for paper and 's' for scissors or 'x' to exit the game")
    user = input()
    if (user == 'x'):
        print("You have chosen to exit the game. Thank you for playing!")
        break
    else: 
        comp = random.choice(['r', 'p', 's'])
        print(" The computer has chosen", comp )

        if (user == 'r' and comp == 's') or (user == 's' and comp == 'p') or (user == 'p' and comp == 'r') :(
            print("You win")
        )
        elif user == comp :(
            print("Its a tie!")
        )
        else : 
            print("You lose")
    

