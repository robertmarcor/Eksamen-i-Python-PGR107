import random
import os

text_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "random_text.txt")

def get_random_word():
    with open(text_file, "r") as file:
        words = file.readlines()
        chosen_word = random.choice(words).strip()
        print("=== FOR EXAM ASSESOR ===")
        print(f"Selected word: {chosen_word}")
        return chosen_word
    
def reveal_word(word, letters):
    for letter in word:
        if letter.lower() in letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("\n")
