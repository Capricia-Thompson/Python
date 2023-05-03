class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {'checking': BankAccount(
            name='Checking'), 'savings': BankAccount(name='Savings', int_rate=0.05)}

    def make_deposit(self, amount, acct):
        self.accounts[acct].deposit(amount)
        print(f"${amount} deposited to {self.accounts[acct].name} account.")
        print(
            f"{self.accounts[acct].name} balance: ${self.accounts[acct].balance}")
        return self

    def make_withdrawal(self, amount, acct):
        self.accounts[acct].deposit(amount)
        print(f"${amount} withdrawn from {self.accounts[acct].name} account.")
        print(
            f"{self.accounts[acct].name} balance: ${self.accounts[acct].balance}")
        return self

    def display_user_balances(self):
        for acct in self.accounts:
            print(
                f"{self.accounts[acct].name} balance: ${self.accounts[acct].balance}")
        return self

    def transfer_money(self, from_acct, to_user, to_acct, amount):
        self.accounts[from_acct].withdraw(amount)
        to_user.accounts[to_acct].deposit(amount)
        print(
            f"${amount} transfered from {self.accounts[from_acct].name} account to {to_user.name}'s {to_user.accounts[to_acct].name}.")
        print(
            f"{self.accounts[from_acct].name} balance: ${self.accounts[from_acct].balance}")
        return self


class BankAccount:
    def __init__(self, name, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.name = name
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
    500, 'checking').make_withdrawal(150, 'checking')

user1.transfer_money('checking', user2, 'savings', 100)

user2.display_user_balances()
