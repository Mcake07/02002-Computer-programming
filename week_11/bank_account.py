class BankAccount:
    def __init__(self,balance):
        if balance >= 0:
            self.balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return amount
        else: 
            return 0
    def get_balance(self):
        return self.balance
    
class OverdraftAccount(BankAccount):
    def __init__(self,balance,overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit
    def withdraw(self, amount):
        if self.balance - amount >= -1 * self.overdraft_limit:
            self.balance -= amount
            return amount
        else: return 0
    