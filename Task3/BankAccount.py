class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    
    def add_interest(self, rate):
        self.balance *= (1 + rate)
        return self.balance
    
    def get_balance(self):
        return self.balance


