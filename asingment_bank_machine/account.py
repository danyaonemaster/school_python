import random


class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = random.randint(500, 2500)

    def display_balance(self):
        print(f"\nYour current balance is: ${self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
            return 0
        if self.balance - amount < -500:
            print("Transaction denied! You can’t go below -500.")
            return 0
        elif self.balance - amount < 0:
            fee = amount * 0.2
            self.balance -= (amount + fee)
            print(f"Overdraft! 20% fee applied. New balance: ${self.balance:.2f}")
            return amount
        else:
            self.balance -= amount
            print(f"Withdrawal successful! New balance: ${self.balance:.2f}")
            return amount

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
            return
        self.balance += amount
        print(f"Deposit successful! New balance: ${self.balance:.2f}")

    def transfer(self, amount, account):
        account.deposit(self.withdraw(amount))
        self.display_balance()
        print(f"{account.username} balance is: ${account.balance}")

    def change_password(self, old ,new):
        if old != self.password:
            print("Invalid old password.")
        else:
            self.password = new
            print(f"You update your password.")


    def exit(self):
        print(f"Goodbye, {self.username}!")
        exit(0)
