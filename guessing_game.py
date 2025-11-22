import random


def play_game():
    """Main function to run the number guessing game"""

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Initialize attempt counter
    attempts = 0

    # Game introduction
    print("\n" + "="*50)
    print("Welcome to the Number Guessing Game!")
    print("="*50)
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    print("="*50 + "\n")

    # Main game loop - continues until player guesses correctly
    while True:
        try:
            # Get player's guess
            guess = int(input("Enter your guess: "))

            # Increment attempt counter
            attempts += 1

            # Check if guess is correct
            if guess == secret_number:
                print(f"\n🎉 Congratulations! You guessed it!")
                print(f"The number was {secret_number}")
                print(f"It took you {attempts} attempts.\n")
                break  # Exit the loop when correct

            # Provide hints if guess is wrong
            elif guess < secret_number:
                print("📈 Too low! Try a higher number.\n")
            else:
                print("📉 Too high! Try a lower number.\n")

        except ValueError:
            # Handle non-numeric input
            print("❌ Invalid input! Please enter a number.\n")


def main():
    """Main program loop with replay option"""

    while True:
        # Play one round of the game
        play_game()

        # Ask if player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()

        if play_again != "yes" and play_again != "y":
            print("\nThanks for playing! Goodbye! 👋\n")
            break


# Start the game when script is run
if __name__ == "__main__":
    main()
