import time

from asingment_bank_machine.account import Account


class BankMachine:
    def __init__(self):
        users = [
            ("swindrunner", "1234"),
            ("istormrage", "abcd"),
            ("tpgallywix", "qwerty")
        ]
        self.accounts = [Account(user, password) for user, password in users]

    def run(self):
        print("Welcome to the ATM Machine!")

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
            print("\n--- MAIN MENU ---")
            print("1. Display Balance         4. Transfer")
            print("2. Withdraw                5. Change Password")
            print("3. Deposit                 6. Logout ")
            print("7. Exit")

            choice = input("Enter choice (1-7): ")

            match choice:
                case "1":
                    account.display_balance()
                case "2":
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                case "3":
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)
                case "4":
                    amount = float(input("Enter amount to deposit: "))
                    run = True
                    while run:
                        other_account = input("Input username of another account: ")
                        for account in self.accounts:

                            if account.username == other_account:
                                account.transfer(amount, account)
                                run = False
                            else:
                                print("Incorrect username.")
                case "5":
                    old_password = input("\nEnter old password: ")
                    new_password = input("\nEnter new password: ")
                    account.change_password(old_password, new_password)
                    time.sleep(2)
                case "6":
                    self.logout(account)
                case "7":
                    account.exit()
                case _:
                    print("Invalid option, try again.")
