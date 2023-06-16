class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful. New balance:", self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal successful. New balance:", self.balance)
        else:
            print("Insufficient funds. Withdrawal failed.")

    def transfer(self, recipient_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient_account.deposit(amount)
            print("Transfer successful. New balance:", self.balance)
        else:
            print("Insufficient funds. Transfer failed.")

    def display_balance(self):
        print("Account Number:", self.account_number)
        print("Owner:", self.owner)
        print("Balance:", self.balance)

# Usage example
account1 = BankAccount("123456789", "John Doe")
account2 = BankAccount("987654321", "Jane Smith", balance=1000)

account1.display_balance()
account2.display_balance()

account1.deposit(500)
account2.withdraw(200)

account1.transfer(account2, 300)

account1.display_balance()
account2.display_balance()
