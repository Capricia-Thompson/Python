class BankAccount:
    all_accounts = []

    def __init__(self, int_rate, balance=0):
        self.int_rate = 0.01
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        print(f"Balance: ${self.balance}")
        return self

    def withdraw(self, amount):
        if (self.balance - amount >= 0):
            self.balance -= amount
            print(f"Balance: ${self.balance}")
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        if (self.balance > 0):
            self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            print(account.balance)
            print(account.int_rate)


acct1 = BankAccount(0.02, 3857)
acct2 = BankAccount(0.05)

acct1.deposit(284).deposit(28).deposit(107).withdraw(
    3856).yield_interest().display_account_info()

acct2.deposit(239).deposit(9375).withdraw(294).withdraw(475).withdraw(
    305).withdraw(3957).yield_interest().display_account_info()

BankAccount.print_all_accounts()
