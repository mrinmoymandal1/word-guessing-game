import random

# Ask the user for their name
name = input("What is your name? ")

# Greet the user
print("Good Luck ! ", name)

# List of words for the game
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

# Choose a random word from the list
word = random.choice(words)

# Number of turns allowed for guessing
turns = 12

# Initialize an empty string to store guessed characters
guesses = ''

# Start the game loop
while turns > 0:

    # Counter for failed guesses
    failed = 0

    # Iterate over each character in the word
    for char in word:
        # Check if the character has been guessed
        if char in guesses:
            # If guessed, print the character
            print(char, end=" ")
        else:
            # If not guessed, print an underscore
            print("_", end=" ")

            # Increment the failed counter
            failed += 1

    # Check if all characters have been guessed
    if failed == 0:
        # If all characters guessed, the user wins
        print("\nYou Win")
        # Display the correct word
        print("The word is: ", word)
        break

    # Ask the user to guess a character
    guess = input("\nguess a character: ")

    # Add the guessed character to the guesses
    guesses += guess

    # Check if the guessed character is not in the word
    if guess not in word:
        # Decrement the turns counter
        turns -= 1
        # Inform the user about the wrong guess
        print("Wrong")
        # Display the number of turns left
        print("You have", + turns, 'more guesses')

        # Check if the user has used all turns
        if turns == 0:
            # If no turns left, the user loses
            print("You Loose")
