letters = []

def input_validation(letter):
    invalid_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?~1234567890"
    if letter.lower() in invalid_characters:
        print("Not a valid guess, please enter something between A-Z")
        return False
    return True

def get_input(word, letters, guesses):
    user_input = input("Enter a letter: ").lower()
    
    if input_validation(user_input):
        if user_input in letters:
            print("You already guessed that letter")
            return None, guesses
        elif user_input in word.lower():
            letters.append(user_input)
            return user_input, guesses
        else:
            letters.append(user_input)
            guesses -= 1
            return user_input, guesses
    
    return None, guesses
