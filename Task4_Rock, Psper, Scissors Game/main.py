import random

# List of possible moves
moves = ['rock', 'paper', 'scissors']

def get_user_move():
    while True:
        user_input = input("Choose rock, paper, or scissors: ").strip().lower()
        if user_input in moves:
            return user_input
        print("Invalid choice. Please try again.")

def get_computer_move():
    return random.choice(moves)

def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (
        (user == 'rock' and computer == 'scissors') or
        (user == 'paper' and computer == 'rock') or
        (user == 'scissors' and computer == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_move = get_user_move()
        computer_move = get_computer_move()
        print(f"You chose: {user_move}")
        print(f"Computer chose: {computer_move}")
        result = decide_winner(user_move, computer_move)
        print(result)
        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
