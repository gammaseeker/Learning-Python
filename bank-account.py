class BankAccount:
   # define a class to simulate a bank account
   def __init__ (self):
      # initialize the bank account with zero balance
      self.balance = 0
   def deposit (self, amount):
      # deposit the given amount into the account
      self.balance = self.balance + amount
   def withdraw (self, amount):
      # withdraw the given amount from the account
      self.balance = self.balance - amount
   def get_balance (self):
      # return the balance in the account
      return self.balance

my_account = BankAccount()
second_account = BankAccount()

my_account.deposit(200)
second_account.deposit(125)
my_account.withdraw(75)
second_account.withdraw(50)

print(my_account.get_balance())
print(second_account.get_balance())

