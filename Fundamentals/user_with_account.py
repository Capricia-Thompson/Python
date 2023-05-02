class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.checking = BankAccount(
            'checking', int_rate=0.02, balance=0)
        self.savings = BankAccount('savings', int_rate=0.02, balance=0)

    def make_deposit(self, amount, account):
        selection = self.select_account(account)
        selection.deposit(amount)
        print(f"${amount} deposited to {account.title()} account.")
        return self

    def make_withdrawal(self, amount, account):
        selection = self.select_account(account)
        selection.withdraw(amount)
        print(f"${amount} withdrawn from {account.title()} account.")
        return self

    def display_user_balance(self):
        print(f"Checking balance: ${self.checking.balance}")
        print(f"Savings balance: ${self.savings.balance}")
        return self

    def select_account(self, account):
        if account == 'checking':
            return self.checking
        elif account == 'savings':
            return self.savings

    def transfer_money(self, from_account, to_user, to_account, amount):
        from_selection = self.select_account(from_account)
        from_selection.withdraw(amount)
        to_selection = to_user.select_account(to_account)
        to_selection.deposit(amount)
        print(
            f"${amount} transfered from {from_account.title()} account to {to_user.name}'s {to_account.title()}.")
        return self


class BankAccount:
    def __init__(self, type, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.type = type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount >= 0):
            self.balance -= amount
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


user1 = User('Amy', 'amy@email.com')
user2 = User('Lynn', 'lynn@email.com')
user3 = User('Bob', 'bob@email.com')

user1.make_deposit(500, 'savings').make_deposit(
    500, 'checking').make_withdrawal(150, 'checking').display_user_balance()

user1.transfer_money('checking', user2, 'savings', 100).display_user_balance()

user2.display_user_balance()
