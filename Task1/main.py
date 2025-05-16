"""
Word Guessing Game

A simple word guessing game

Program explanation:
We select a random word from a text file "random_text.txt".
We declare global variables at the beginning which controls the game.
While the player has guesses left, the game will continue untill out of guesses.

Each guess is validated to make sure it's a letter between A-Z.
If the guess is incorrect, the player loses a guess.
If the guess is correct, the letter is added to the list of letters
and we reveal the word with the guessed letters.

Program does not care about case sensitivity, and does not care if you input
more than one letter at a time. It says "Enter a letter" and will punish you
for wrong input :)

word is handled in random_word.py
input is handled in user_input.py

Win Condition:
The player wins by guessing all letters in the word.

Lose Condition:
The player loses by running out of guesses.



"""
from random_word import get_random_word, reveal_word
from user_input import get_input

word = get_random_word()
guesses = len(word)
letters = []


if __name__ == "__main__":
    print("\n╔═══════════════════════════════════════╗")
    print("║          WORD GUESSING GAME           ║")
    print("╚═══════════════════════════════════════╝")
    print(f"\nYou have {guesses} guesses to guess the word")
    print(f"The WORD is {len(word)} letters long")
    print("\n═════════════════════════════════════")
    print("             GAME START               ")
    print("═════════════════════════════════════")
    

    # For display purposes, blank word
    reveal_word(word, letters) 
    
    loop_counter = 0
    print(f"\n═════════ Guess Counter: {loop_counter} ═════════")
    while guesses > 0:
        hearts = "♥ " * guesses
        print(f"Guesses remaining: ({guesses}) {hearts}")
        
        user_guess, guesses = get_input(word, letters, guesses)
        
        # if the input was valid
        if user_guess:
            if user_guess in word.lower():
                print("✅ Correct!\n")
            else:
                print("❌ Incorrect!\n")
        loop_counter += 1
                
        reveal_word(word, letters)
            
        print(f"\n═════════ Guess Counter: {loop_counter} ═════════")
        
        # Check if all letters in the word have been guessed (case-insensitive)
        if all(letter.lower() in letters for letter in word):
            print("\n═══════════════════════════════════════")
            print("            🎉 You win! 🎉             ")
            print("═══════════════════════════════════════")
            break
    
    # Game over
    if guesses == 0:
        print("\n═══════════════════════════════════════")
        print("            💀 You lose! 💀")
        print("═══════════════════════════════════════")
        print(f"The word was: {word}")

