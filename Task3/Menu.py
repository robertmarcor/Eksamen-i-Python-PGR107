import os
import time
from BankAccount import BankAccount

class Menu:
    def __init__(self):
        self.menu_options = []

    def add_option(self, option):
        self.menu_options.append(option)

    def get_input(self):
        self.display_menu()
        return input(self.menu_options)
    
    def display_menu(self):
        self.display_header()
        for option in self.menu_options:
            print(option)
        print("\n")
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def add_all_options(self):
        self.menu_options = []
        self.add_option("1. 💰 Open a new account")
        self.add_option("2. 💵 Deposit money into your account")
        self.add_option("3. 💸 Withdraw money from your account")
        self.add_option("4. 📈 Add interests to your account (2.5%)")
        self.add_option("5. 💼 Get the current balance of your account")
        self.add_option("6. 👋 Quit")
    
    def display_header(self, operation=None):
        if operation is None:
            header = """
╔═══════════════════════════════════════╗
║         BANK ACCOUNT SYSTEM           ║
╚═══════════════════════════════════════╝
"""
        elif operation == "new_account":
            header = """
═════════════════════════════════════
           NEW ACCOUNT CREATED       
═════════════════════════════════════
"""
        elif operation == "deposit":
            header = """
═════════════════════════════════════
           DEPOSIT SUCCESSFUL        
═════════════════════════════════════
"""
        elif operation == "withdraw":
            header = """
═════════════════════════════════════
          WITHDRAWAL SUCCESSFUL      
═════════════════════════════════════
"""
        elif operation == "interest":
            header = """
═════════════════════════════════════
           INTEREST ADDED            
═════════════════════════════════════
"""
        elif operation == "balance":
            header = """
═════════════════════════════════════
          ACCOUNT BALANCE            
═════════════════════════════════════
"""
        elif operation == "exit":
            header = """
═════════════════════════════════════
THANK YOU FOR USING THE BANKING SYSTEM 
═════════════════════════════════════
"""
        elif operation == "error":
            header = """
═════════════════════════════════════
              ERROR                  
═════════════════════════════════════
"""
        print(header)
        
    def display_account_status(self, account=None):
        if account is None:
            print("💰 Account Status: No account open")
            print("═════════════════════════════════════\n")
        else:
            print(f"💰 Account Status: Active - Balance: ${account.get_balance():.2f}")
            print("═════════════════════════════════════\n")
    
    def display_welcome_screen(self):
        self.clear_screen()
        print("\n╔═══════════════════════════════════════╗")
        print("║      BANK ACCOUNT MANAGEMENT SYSTEM   ║")
        print("╚═══════════════════════════════════════╝")
        
        print("\nInitializing system...")
        time.sleep(0.5)
        print("✓ System ready!")
    
    def check_account_exists(self, account):
        """Check if an account exists and display error if not"""
        if account is None:
            self.display_header("error")
            print("❌ You need to open an account first (Option 1)")
            return False
        return True
    
    def create_account_menu(self):
        initial_balance = 0
        print("\nCreating account...")
        time.sleep(0.5)
        account = BankAccount(initial_balance)
        self.display_header("new_account")
        print(f"✓ Account created successfully, current balance: ${account.get_balance():.2f}")
        return account
    
    def deposit_menu(self, account):
        if not self.check_account_exists(account):
            return account
        
        while True:
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount <= 0:
                    self.display_header("error")
                    print("❌ Deposit amount must be positive")
                    continue
                
                print("\nProcessing deposit...")
                time.sleep(0.5)
                account.deposit(amount)
                self.display_header("deposit")
                print(f"✓ Deposit successful! New balance: ${account.get_balance():.2f}")
                break
            except ValueError:
                self.display_header("error")
                print("❌ Please enter a valid number")
                continue
        
        return account
    
    def withdraw_menu(self, account):
        if not self.check_account_exists(account):
            return account
        
        # Dont proceed if balance is invalid
        current_balance = account.get_balance()
        if current_balance <= 0:
            self.display_header("error")
            print(f"❌ Cannot withdraw funds. Your balance is ${current_balance:.2f}")
            print("   Please deposit money first.")
            return account
        
        while True:
            try:
                print(f"Current balance: ${current_balance:.2f}")
                
                amount = float(input("Enter amount to withdraw: "))
                if amount <= 0:
                    self.display_header("error")
                    print("❌ Withdrawal amount must be positive")
                    continue
                elif amount > current_balance:
                    self.display_header("error")
                    print(f"❌ Insufficient funds. Your balance is ${current_balance:.2f}")
                    # Ask if they want to try again or return to main menu
                    retry = input("Would you like to try another amount? (y/n): ")
                    if retry.lower() != 'y':
                        break
                    continue
                
                print("\nProcessing withdrawal...")
                time.sleep(0.5)
                account.withdraw(amount)
                self.display_header("withdraw")
                print(f"✓ Withdrawal successful! New balance: ${account.get_balance():.2f}")
                break
            except ValueError:
                self.display_header("error")
                print("❌ Please enter a valid number")
                continue
        
        return account
    
    def interest_menu(self, account):
        if not self.check_account_exists(account):
            return account
        
        # Dont proceed if balance is invalid
        current_balance = account.get_balance()
        if current_balance <= 0:
            self.display_header("error")
            print(f"❌ Cannot add interest. Your balance is ${current_balance:.2f}")
            print("   Interest can only be added to positive balances.")
            return account
        
        # Use fixed 2.5% interest rate
        rate = 0.025
        print("\nCalculating interest at 2.5% rate...")
        time.sleep(0.5)
        account.add_interest(rate)
        self.display_header("interest")
        print(f"✓ Interest added! New balance: ${account.get_balance():.2f}")
        
        return account
    
    def balance_menu(self, account):
        if not self.check_account_exists(account):
            return account
        
        print("\nRetrieving balance information...")
        time.sleep(0.5)
        self.display_header("balance")
        print(f"Current balance: ${account.get_balance():.2f}")
        return account
    
    def exit_menu(self):
        self.display_header("exit")
        print("Thank you for using the Bank Account Management System!")
        return False
        
    def get_valid_choice(self):
        while True:
            choice = input("Enter your choice (1-6): ")
            
            if choice in ["1", "2", "3", "4", "5", "6"]:
                return choice
            else:
                self.display_header("error")
                print("❌ Invalid choice. Please select a number between 1-6.")


