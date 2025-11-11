import random


class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = random.randint(500, 2500)
        self.history = []

    def display_balance(self):
        print(f"\nYour current balance is: ${self.balance}")

    def withdraw(self, amount, silent=False):
        if amount <= 0:
            if not silent:
                print("Invalid amount.")
            return 0

        if self.balance - amount < -500:

            if not silent:
                print("Transaction denied! You can’t go below -500.")
            return 0

        elif self.balance - amount < 0:
            fee = amount * 0.2
            self.balance -= (amount + fee)

            if not silent:
                print(f"Overdraft! 20% fee applied. New balance: ${self.balance:.2f}")
            self.history.append(f"Withdraw: {amount} with interest")
            return 1

        else:
            self.balance -= amount
            if not silent:
                print(f"Withdrawal successful! New balance: ${self.balance:.2f}")
            self.history.append(f"Withdraw: {amount}")
            return 1

    def deposit(self, amount, silent=False):
        if amount <= 0:
            if not silent:
                print("Invalid deposit amount.")
            return
        self.balance += amount
        if not silent:
            print(f"Deposit successful! New balance: ${self.balance:.2f}")
        self.history.append(f"Deposit: +${amount}")

    def transfer(self, amount, account):
        if self.withdraw(amount, silent=True) == 0:
            print("Transfer failed! Not enough funds.")
            return 0

        account.deposit(amount, silent=True)
        self.history.append(f"Transfer to {account.username}: -${amount}")
        account.history.append(f"Transfer from {self.username}: +${amount}")

        print(f"Transfer to {account.username} successful! Amount: ${amount}")
        return 1

    def get_summary(self):
        print(f"\n👤 Account Summary for {self.username}")
        print(f"🏦 Current Balance: ${self.balance:.2f}")
        print("🕒 Last 3 transactions:\n")

        if not self.history:
            print("No transactions yet.")
        else:
            for transaction in self.history[-3:][::-1]:
                print(f" - {transaction}")

    def change_password(self, old, new):
        if old != self.password:
            print("Invalid old password.")
            return

        if not new.strip():
            print("Password cannot be empty.")
            return

        self.password = new
        print("Password updated successfully!")

    def exit(self):
        print(f"Goodbye, {self.username}!")
        exit(0)
