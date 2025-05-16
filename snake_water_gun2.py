import random

def snake_water_gun_game():
    # Define the options
    options = ["Snake", "Water", "Gun"]

    # Define the result matrix
    # Rows represent user choices, columns represent computer choices.
    # 0: Tie, 1: User wins, -1: Computer wins
    result_matrix = [
        [0, 1, -1],  # User chooses Snake
        [-1, 0, 1],  # User chooses Water
        [1, -1, 0]   # User chooses Gun
    ]

    print("Welcome to Snake-Water-Gun game!")
    print("Options: 1 for Snake, 2 for Water, 3 for Gun")

    try:
        # Get user input
        user_choice = int(input("Enter your choice (1/2/3): ")) - 1
        if user_choice not in [0, 1, 2]:
            print("Invalid choice! Please enter 1, 2, or 3.")
            return

        # Generate computer's choice
        computer_choice = random.randint(0, 2)

        # Display choices
        print(f"You chose: {options[user_choice]}")
        print(f"Computer chose: {options[computer_choice]}")

        # Determine the result
        result = result_matrix[user_choice][computer_choice]

        # Display the result
        if result == 0:
            print("It's a tie!")
        elif result == 1:
            print("You win!")
        else:
            print("Computer wins!")

    except ValueError:
        print("Invalid input! Please enter a number (1/2/3).")

# Run the game
if __name__ == "__main__":
    snake_water_gun_game()
