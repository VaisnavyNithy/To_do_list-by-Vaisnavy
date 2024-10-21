import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors!")
    print("Choose rock, paper, or scissors. Type 'exit' to quit the game.")

    while True:
        user_choice = input("Enter your choice: ").lower()
        
        if user_choice == 'exit':
            break
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"Scores -> You: {user_score}, Computer: {computer_score}")

        # Ask if user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")
    print(f"Final Scores -> You: {user_score}, Computer: {computer_score}")

if __name__ == "__main__":
    main()
