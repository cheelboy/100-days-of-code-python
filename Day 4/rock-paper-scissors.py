import random

choices = ["rock", "paper", "scissors"]

choose = input('Type "1" for Rock. "2" for Paper. "3" for Scissors: ')

user_choice = int(choose) - 1
computer_choice = random.randint(0, 2)

user_choice = choices[user_choice]
computer_choice = choices[computer_choice]

if computer_choice == "rock" and user_choice == "paper":
    print(f"You chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    print("You win! :D".upper())
elif computer_choice == "rock" and user_choice == "scissors":
    print(f"You chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    print("You lose. :(".upper())
elif computer_choice == "paper" and user_choice == "scissors":
    print(f"You chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    print("You win! :D".upper())
elif computer_choice == "paper" and user_choice == "rock":
    print(f"You chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    print("You lose! :(".upper())
elif computer_choice == "scissors" and user_choice == "rock":
    print(f"You chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    print("You win! :D".upper())
elif computer_choice == "scissors" and user_choice == "paper":
    print(f"You chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    print("You lose! :(".upper())
elif computer_choice == user_choice:
    print(f"You chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    print("It's a draw! :|".upper())
else:
    print("Type a valid number.")
