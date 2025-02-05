import random

def generate_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def decide_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

def start_game():
    player_score = 0
    cpu_score = 0

    while True:
        print("\nWelcome to Rock, Paper, Scissors!")
        print("Please choose: rock, paper, or scissors.")
        
        player_choice = input("Enter your choice: ").lower()
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please choose rock, paper, or scissors.")
            continue
        
        cpu_choice = generate_computer_choice()
        print(f"Computer picked: {cpu_choice}")
        
        result = decide_winner(player_choice, cpu_choice)
        
        if result == "tie":
            print("It's a tie!")
        elif result == "win":
            print("You win!")
            player_score += 1
        else:
            print("You lose!")
            cpu_score += 1

        print(f"Current score - You: {player_score} | Computer: {cpu_score}")
        
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing!")
            break

start_game()
