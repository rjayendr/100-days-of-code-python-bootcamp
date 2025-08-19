rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_art = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices_ascii = {
    "rock": rock_art,
    "paper": paper_art,
    "scissors": scissors_art
}

validChoices = ["rock", "paper", "scissors"]
import random
print("Welcome to Rock, Paper, Scissors!\n")
print("Enter 'Quit' to exit the game at any time.\n")

while True:
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice == "quit":
        print("Thanks for playing!")
        break
    if user_choice not in validChoices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(validChoices) 
    print(f"You chose: {user_choice}\n{choices_ascii[user_choice]}")
    print(f"Computer chose: {computer_choice}\n{choices_ascii[computer_choice]}")
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == "rock" and computer_choice == "scissors"):
        print("You win! Rock crushes scissors.")
    elif (user_choice == "paper" and computer_choice == "rock"):
        print("You win! Paper covers rock.")
    elif (user_choice == "scissors" and computer_choice == "paper"):
        print("You win! Scissors cut paper.")
    else:
        print("You lose!")  

