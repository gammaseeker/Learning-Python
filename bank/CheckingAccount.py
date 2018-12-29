class CheckingAccount(BankAccount):
    def __init__(self, initBal):
        BankAccount.__init__(self, init_bal)
        self.check_record = {}

    def process_check(self, number, to_who, amount):
        self.withdraw(amount)
        self.check_record[number] = (to_who, amount)
    
    def check_info(self, number):
        if self.check_record.has_key(number):
            return self.check_record[number]
        else:
            return 'no such check'

def main():
    my_acct = CheckingAccount()
    my_acct
