""" 
Task3 Bank Account Management System 

Menuing program for bank account management,
a bit like the previous task as I may have done more than what was asked for hehe.

same concept as Task2, just without the automatic test script
and moving the menu logic to the Menu class for better encapsulation and following object-oriented principles better

We have 2 objects
- BankAccount
- Menu

BankAccount has 4 methods
- deposit
- withdraw
- add_interest
- get_balance

the methods are quite self explanatory and does what you expect them to do.
deposit and withdraw - adds or subtracts from the balance
add_interest - multiplies the balance by a certain interest rate ( my assumption on how to do it )
get_balance - returns the balance

Menu class handles menu operations:
- Displaying menus and headers
- Processing user input
- Managing account operations through specialized menu methods
- Providing methods for the main loop to call

Main program:
Creates the menu object and adds all options to it.
controls the flow of the program and calls the menu methods to handle the user input.
we also dont want the user to access menu options when they dont have an account.
There are also guards for trying to withdraw or add interest when the balance is 0 or negative.
"""
from Menu import Menu

def main():
    """Main program loop"""
    
    # Create menu and initialize
    menu = Menu()
    menu.add_all_options()
    
    # Initialize account to None because we want the user to create an accounnt through the menu
    account = None
    
    menu.display_welcome_screen()
    running = True
    
    while running:
        menu.clear_screen()
        menu.display_menu()
        menu.display_account_status(account)
        
        choice = menu.get_valid_choice()
        
        menu.clear_screen()
        
        if choice == "1":
            account = menu.create_account_menu()
        elif choice == "2":
            account = menu.deposit_menu(account)
        elif choice == "3":
            account = menu.withdraw_menu(account)
        elif choice == "4":
            account = menu.interest_menu(account)
        elif choice == "5":
            account = menu.balance_menu(account)
        elif choice == "6":
            running = menu.exit_menu()
        
        if running:
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

