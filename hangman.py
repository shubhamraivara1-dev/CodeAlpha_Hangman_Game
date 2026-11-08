import random

def hangman():
    # Predefined word list
    words = ["python", "coding", "alpha", "intern", "github"]
    secret_word = random.choice(words)
    
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("=" * 40)
    print("      🎮 Welcome to Hangman Game 🎮")
    print("=" * 40)
    print(f"You have {max_incorrect} incorrect guesses allowed.\n")

    while incorrect_guesses < max_incorrect:
        # Display current word status
        display_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
        print("Word: " + " ".join(display_word))
        print(f"Remaining chances: {max_incorrect - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")

        # Check if user won
        if "_" not in display_word:
            print("\n" + "=" * 40)
            print(f"🎉 Congratulations! You guessed the word: {secret_word.upper()}")
            print("=" * 40)
            return

        guess = input("\nEnter a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter! Try another one.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f"❌ Oops! '{guess}' is not in the word.\n")

    # If all chances are used
    print("=" * 40)
    print(f"💀 Game Over! The word was: {secret_word.upper()}")
    print("=" * 40)

if __name__ == "__main__":
    hangman()