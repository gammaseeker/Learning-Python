class BankAccount():
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def get_balance(self):
        return self.balance

def main():
    my_account = BankAccount()
    print(my_account.get_balance())
    my_account.deposit(200)
    print(my_account.get_balance())

main()
