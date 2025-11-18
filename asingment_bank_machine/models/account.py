import random

from asingment_bank_machine.utils import utils


class Account:
    def __init__(self, username, password):
        # Basic account data
        self.username = username
        self.password = password

        # Random starting balance between 500 and 2500
        self.balance = random.randint(500, 2500)

        # List to store transaction history
        self.history = []

    def display_balance(self):
        # Simply prints the current balance
        print(f"Your current balance is: ${self.balance}")

    def withdraw(self, amount, silent=False):
        # Check for invalid withdrawal
        if amount <= 0:
            Account.print("Invalid amount.", silent)
            return 0

        # Money available before going into overdraft
        available = max(self.balance, 0)

        # How much the user is trying to withdraw beyond available funds
        overdraft = max(0, amount - available)

        # 20% fee applied to the overdraft portion
        commission = overdraft * 0.2

        # New balance after withdrawal and commission
        new_balance = self.balance - amount - commission

        # Prevent user from going below –500
        if new_balance < -500:
            Account.print("Transaction denied! You can’t go below -500.", silent)
            return 0

        # If overdraft is used
        if overdraft > 0:
            Account.print(
                f"Overdraft! 20% fee applied. New balance: ${new_balance:.2f}",
                silent
            )
            self.history.append(f"Withdraw: {amount} with interest {commission}")
            self.balance = new_balance
            return 1

        # Regular withdrawal
        self.balance = new_balance
        self.history.append(f"Withdraw: {amount}")
        Account.print(f"Withdrawal successful! New balance: ${self.balance:.2f}", silent)
        return 1

    def deposit(self, amount, silent=False):
        # Invalid deposit check
        if amount <= 0:
            Account.print("Invalid deposit amount.", silent)
            return

        # Add money to balance
        self.balance += amount
        Account.print(f"Deposit successful! New balance: ${self.balance:.2f}", silent)

        # Add to history
        self.history.append(f"Deposit: +${amount}")

    def transfer(self, amount, account):
        # Try to withdraw from the sender (silent mode prevents extra messages)
        if self.withdraw(amount, silent=True) == 0:
            print("Transfer failed! Not enough funds.")
            return 0

        # Deposit into the receiver
        account.deposit(amount, silent=True)

        # Record transactions for both accounts
        self.history.append(f"Transfer to {account.username}: -${amount}")
        account.history.append(f"Transfer from {self.username}: +${amount}")

        print(f"Transfer to {account.username} successful! Amount: ${amount}")
        return 1

    def get_summary(self):
        # Show account summary and last 3 transactions
        print(f"\n👤 Account Summary for {self.username}")
        print(f"🏦 Current Balance: ${self.balance:.2f}")
        print("🕒 Last 3 transactions:\n")

        if not self.history:
            print("No transactions yet.")
        else:
            # Display last 3, newest first
            for transaction in self.history[-3:][::-1]:
                print(f" - {transaction}")

    def change_password(self, old, new):
        # Verify old password
        if old != self.password:
            print("Invalid old password.")
            return

        # Ensure new password is not empty
        if not new.strip():
            print("Password cannot be empty.")
            return

        # Update password
        self.password = new
        print("Password updated successfully!")

    def exit(self):
        # Play animation and exit program
        utils.loading_animation("ATM exiting", f"Goodbye, {self.username}!")
        exit(0)

    @staticmethod
    def print(message: str, silent: bool):
        """
        Prints a message only if silent=False.
        Useful for operations where we want to hide intermediate output.
        """
        if not silent:
            print(message)
