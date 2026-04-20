import random

options = ["rock", "paper", "scissors"]

print("--- Welcome to Rock, Paper, Scissors! ---")

while True:
    # Computer chooses a NEW move every round
    comp_choice = random.choice(options)
    
    user_choice = input("\nEnter rock, paper, or scissors: ").lower()

    if user_choice not in options:
        print("Invalid choice!")
        continue # Skip the rest of the loop and ask for input again

   

    # Game Logic
    if user_choice == comp_choice:
        print("It's a Tie!")
    
    # We use parentheses here to keep the 'and' logic clear
    elif (user_choice == "rock" and comp_choice == "paper") or \
         (user_choice == "paper" and comp_choice == "scissors") or \
         (user_choice == "scissors" and comp_choice == "rock"):
        print("You lost!")
    
    else:
        print("Congratulations, you win!")
     # Display the choices
    print(f"Computer choose: {comp_choice}")

    # Global "Play Again" Menu
    print("\n1: Play Again")
    print("2: Exit")
    choice = input("Choose (1-2): ")
    if choice != "1":
        print("Thanks for playing!")
        break