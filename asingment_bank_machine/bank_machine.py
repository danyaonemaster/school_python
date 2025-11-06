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
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            for account in self.accounts:
                if username == account.username and account.password == password:
                    print(f"Login successful! Welcome, {username}.")
                    account = Account(username, password)
                    self.main_menu(account)
                    break
                else:
                    print("Incorrect username or password.")
                    again = input("Try again? (y/n): ").lower()
                    if again != "y":
                        print("Exiting ATM...")
                        break

    def main_menu(self, account):
        while True:
            print("\n--- MAIN MENU ---")
            print("1. Display Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Exit")

            choice = input("Enter choice (1-5): ")

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
                    other_account = input("Enter another account: ")
                    amount = float(input("Enter amount to deposit: "))
                    account.transfer(amount, self.accounts[1])
                case "5":
                    account.exit()
                    break
                case _:
                    print("Invalid option, try again.")
