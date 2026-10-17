class BankAccount:
    def __init__(self, holder_name, account_balance):
        self.holder_name = holder_name
        self.account_balance = account_balance

    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.account_balance = self.account_balance + deposit_amount
            print("Deposit successful.")
        else:
            print("Enter a positive amount.")

    def display(self):
        print("Account holder:", self.holder_name)
        print("Balance:", self.account_balance)

bank_obj = BankAccount("Neha", 1000)
bank_obj.deposit(500)
bank_obj.display()
