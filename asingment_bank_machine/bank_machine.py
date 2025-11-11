from asingment_bank_machine.account import Account


# -------------------------------------
# 🔹 Initialization
# -------------------------------------

class BankMachine:
    def __init__(self):
        users = [
            ("swindrunner", "1234"),
            ("istormrage", "abcd"),
            ("tpgallywix", "qwerty")
        ]
        self.accounts = [Account(user, password) for user, password in users]

# -------------------------------------
# 🔹 User Interface Logic
# -------------------------------------

    def run(self):
        print("\n" + "=" * 40)
        print("💳 Welcome to the Bank Machine 💳")
        print("=" * 40)

        while True:
            username = input("\nEnter your username: ")
            password = input("Enter your password: ")
            sing_in = False
            for account in self.accounts:

                if username == account.username and account.password == password:
                    print(f"\nLogin successful! Welcome, {username}.")
                    account = Account(username, password)
                    self.main_menu(account)
                    sing_in = True
                    break

            if not sing_in:
                print("Incorrect username or password.")
                again = input("\nTry again? (y/n): ").lower()

                if again != "y":
                    print("Exiting ATM...")
                    exit(0)

    def logout(self, account):
        logout = input("\nDo you really want to logout? (y/n): ").lower()

        if logout == "y":
            print("Logout successful!\n")
            self.run()
        else:
            self.main_menu(account)

    def main_menu(self, account):
        while True:
            print("\n" + "=" * 40)
            print(f"🏦 Welcome, {account.username}")
            print("=" * 40)
            print("1️⃣  Display Balance         4️⃣  Transfer")
            print("2️⃣  Withdraw                5️⃣  Get History")
            print("3️⃣  Deposit                 6️⃣  Change Password")
            print("7️⃣  Logout                  8️⃣  Exit")
            print("=" * 40)

            choice = input("Enter choice (1-8): ").strip()
            print()

            match choice:
                case "1":
                    account.display_balance()

                case "2":
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount) if amount > 0 else 0

                case "3":
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)

                case "4":
                    amount = float(input("Enter amount to transfer: "))
                    other_username = input("Enter recipient username: ")
                    recipient = self.find_account(other_username)

                    if recipient:
                        account.transfer(amount, recipient)
                    else:
                        print("Account not found.")

                case "5":
                    account.get_summary()

                case "6":
                    old_password = input("\nEnter old password: ")
                    new_password = input("\nEnter new password: ")
                    account.change_password(old_password, new_password)

                case "7":
                    self.logout(account)

                case "8":
                    account.exit()

                case _:
                    print("Invalid option, try again.")

# -------------------------------------
# 🔹 Helper / Utility Functions
# -------------------------------------

    def find_account(self, username):
        for acc in self.accounts:
            if acc.username == username:
                return acc
        return None
