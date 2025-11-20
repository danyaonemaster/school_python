from asingment_bank_machine.models.account import Account
from asingment_bank_machine.utils import slowio, utils
from asingment_bank_machine.static_data.pr_text import *


# -------------------------------------
# 🔹 ATM System (BankMachine)
# -------------------------------------

class BankMachine:
    def __init__(self):
        """
        Initialize the ATM with a preset list of users.
        Each user gets a new Account object.
        """
        users = [
            ("swindrunner", "1234"),
            ("istormrage", "abcd"),
            ("tpgallywix", "qwerty")
        ]
        # Create Account objects for each user
        self.accounts = [Account(user, password) for user, password in users]

    # -------------------------------------
    # 🔹 Main ATM Loop / Login Logic
    # -------------------------------------

    def run(self):
        """
        Run the ATM system.

        Handles the login loop:
        - Prompts the user for username and password.
        - Verifies authentication.
        - Redirects to the main menu after successful login.

        Loops until the user logs in correctly or exits.
        """
        slowio.enable()

        # Display welcome screen with slow-print effect
        for line in welcome:
            print(line)

        # Main login loop
        while True:
            username = input("\nEnter your username: ")
            password = input("Enter your password: ")
            print()

            sing_in = False

            # Check credentials
            for account in self.accounts:

                if username == account.username and account.password == password:

                    # Show login animation
                    utils.loading_animation("try to login",
                                            f"Login successful! Welcome, {username}.")

                    # Enter main menu
                    self.main_menu(account)
                    sing_in = True
                    break

            # If login failed
            if not sing_in:
                utils.loading_animation("try to login", "Incorrect username or password.")
                again = input("\nTry again? (y/n): ").lower()

                if again != "y":
                    utils.loading_animation("Exiting ATM", 0)
                    exit(0)

    # -------------------------------------
    # 🔹 Logout
    # -------------------------------------

    def logout(self, account):
        """
        Log the user out of the system.

        Args:
            account (Account): The currently logged-in user.

        Behavior:
        - Confirms logout.
        - Returns to login menu if confirmed.
        - Otherwise returns to main menu.
        """
        logout = input("\nDo you really want to logout? (y/n): ").lower()

        if logout == "y":
            print("Logout successful!\n")
            self.run()
        else:
            self.main_menu(account)

    # -------------------------------------
    # 🔹 Main ATM Menu
    # -------------------------------------

    def main_menu(self, account):
        """
         Display and handle the main ATM menu.

         Args:
             account (Account): The currently logged-in account.

         Allows user to:
         - Check balance
         - Withdraw
         - Deposit
         - Transfer funds
         - View last transactions
         - Change password
         - Logout
         - Exit program
         """
        while True:
            print("\n" + "=" * 40)
            print(f"🏦 Welcome, {account.username}")

            # Print menu lines from external file
            for line in menu:
                print(line)

            choice = input("Enter choice (1-8): ").strip()

            # Short animation for effect
            utils.loading_animation(completion_message=' ')

            match choice:

                # BALANCE
                case "1":
                    account.display_balance()
                    utils.timer()

                # WITHDRAW
                case "2":
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount) if amount > 0 else 0

                # DEPOSIT
                case "3":
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)

                # TRANSFER
                case "4":
                    amount = float(input("Enter amount to transfer: "))
                    other_username = input("Enter recipient username: ")
                    recipient = self.find_account(other_username)

                    if recipient:
                        account.transfer(amount, recipient)
                    else:
                        print("Account not found.")

                # HISTORY SUMMARY
                case "5":
                    account.get_summary()

                # CHANGE PASSWORD
                case "6":
                    old_password = input("\nEnter old password: ")
                    new_password = input("\nEnter new password: ")
                    account.change_password(old_password, new_password)

                # LOGOUT
                case "7":
                    self.logout(account)

                # EXIT ATM
                case "8":
                    account.exit()

                # INVALID CHOICE
                case _:
                    print("Invalid option, try again.")

    # -------------------------------------
    # 🔹 Utility: Find user account
    # -------------------------------------

    def find_account(self, username):
        """
        Find an account by username.

        Args:
            username (str): Username to search for.

        Returns:
            Account | None:
                - Account object if found
                - None if not found
        """
        for acc in self.accounts:
            if acc.username == username:
                return acc
        return None
