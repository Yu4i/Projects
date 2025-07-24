import random

def game():
    print("Hello, Welcome to the Guessing Game, Please Select a Level")
    print("Easy (10 Chances)\nMedium (5 Chances)\nHard af (1 Chance)")

    chances = {
        "easy": 10,
        "medium": 5,
        "hard af": 1
    }
    
    ranges = {
        "easy": 10,
        "medium": 20,
        "hard af": 50
    }

    options = ["easy", "medium", "hard af"]

    while True:
        choice = input("Enter your choice: ").lower().strip()
        
        if choice in options:
            print(f"You have selected {choice.title()} level.")
            break
        else:
            print("Invalid choice, please select a valid level.")

    # Now you can use the choice:
    num_chances = chances[choice]
    print(f"You have {num_chances} chances. Let the game begin!")

    # Add your guessing logic here...


        
    
    user_tries = chances[choice]
    max_number = ranges[choice]
    random_number = random.randint(1, max_number)
    
    if choice == "easy":
        while user_tries > 0:
            guesses = int(input("Enter Your guess"))  
            if guesses == random_number:
                print("you win")
                break
            else:
                print("oops, Try again")
                user_tries -= 1
                
    if choice == "medium":
        while user_tries > 0:
            guesses = int(input("Enter Your guess"))  
            if guesses == random_number:
                print("you win")
                break
            else:
                print("oops, Try again")
                user_tries -= 1
                
    if choice == "hard af":
        while user_tries > 0:
            guesses = int(input("Enter Your guess"))  
            if guesses == random_number:
                print("you win")
                break
            else:
                print("oops, Try again")
                user_tries -= 1


                
         
       
    

    
   

    
game()