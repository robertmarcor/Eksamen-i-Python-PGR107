""" 
Task 4 Palindrome Reader
Simple program to reverse a string and check if its a palindrome.

we take an input and sanitize it to remove all non-alphabetic characters.
then we reverse the string and save it to a variable.
we then use the is_palindrome function to check if the string is a palindrome.
by comparing the original string with the reversed string.

then print the results in the terminal.

loops until the user wants to quit.
"""
import os

def sanitize_string(text):
    return ''.join(char for char in text.lower() if char.isalpha())

def reverse_string(text):
    return text[::-1]

def is_palindrome(text, reverse_text):
    return text == reverse_text

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_input(prompt):
    return input(prompt)

def display_results(original_text, reversed_text, is_palindrome_result):
    print("\nResults:")
    print(f"Original text: {original_text}")
    print(f"Reversed text: {reversed_text}")
    
    if is_palindrome_result:
        print("\n✅ This IS a palindrome!")
    else:
        print("\n❌ This is NOT a palindrome.")

if __name__ == "__main__":
    running = True
    while running:
        clear_screen()
        print("===== PALINDROME CHECKER =====")
        print("A palindrome reads the same forwards and backwards.")
        print("Examples: anna, civic, level or hannah\n")
        
        text = get_input("Enter a string to check: ")
        
        # Make sure to not check empty strings
        if text:
            clean_text = sanitize_string(text)
            reversed_clean_text = reverse_string(clean_text)
            
            if clean_text:
                palindrome_result = is_palindrome(clean_text, reversed_clean_text)
                display_results(text, reverse_string(text), palindrome_result)
            else:
                print("\n No text after sanitizing.")
        else:
            print("\nYou didn't enter any text.")
        
        print("\n -------------------------")
        play_again = get_input("Would you like to check another string? (y/n): ").lower()
        
        if play_again != 'y':
            running = False
            print("\nThank you for using the Palindrome Checker!")
    

