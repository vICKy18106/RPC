import random

def comp_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'user'
    else:
        return 'computer'

def print_choices(user, computer):
    print(f"\nYou chose: {user}")
    print(f"The computer chose: {computer}")

def print_result(result):
    if result == 'tie':
        print("It's a tie!")
    elif result == 'user':
        print("You win!")
    else:
        print("You lose!")

def main():
    user_score = 0
    comp_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        while True:
            user = input("Choose rock, paper, or scissors: ").lower()
            if user in ['rock', 'paper', 'scissors']:
                break
            print("Invalid choice. Please choose rock, paper, or scissors.")

        computer = comp_choice()

        result = determine_winner(user, computer)
        print_choices(user, computer)
        print_result(result)

        if result == 'user':
            user_score += 1
        elif result == 'computer':
            comp_score += 1

        print(f"\nScore - You: {user_score} | Computer: {comp_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("\nThank you for playing Rock, Paper, Scissors!")
    print(f"Final Score - You: {user_score} | Computer: {comp_score}")

if __name__ == "__main__":
    main()
