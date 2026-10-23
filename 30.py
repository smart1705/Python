class InsufficientBalanceError(Exception):
    pass


class AccountClosedError(Exception):
    pass


class Account:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance
        self.closed = False
        self.history = ["Account created"]

    def check_open(self):
        if self.closed:
            raise AccountClosedError("Account is closed.")

    def deposit(self, amount):
        self.check_open()

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        self.balance += amount
        self.history.append("Deposited Rs. " + str(round(amount, 2)))
        print("Deposit successful.")

    def withdraw(self, amount):
        self.check_open()

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance.")

        self.balance -= amount
        self.history.append("Withdrawn Rs. " + str(round(amount, 2)))
        print("Withdrawal successful.")

    def calculate_interest(self):
        return 0

    def display(self):
        print("\nAccount Number:", self.account_no)
        print("Customer Name:", self.name)
        print("Account Type:", type(self).__name__)
        print("Balance: Rs.", round(self.balance, 2))
        print("Status:", "Closed" if self.closed else "Active")

    def show_history(self):
        print("\n--- Transaction History ---")

        if not self.history:
            print("No transactions found.")
        else:
            for item in self.history:
                print(item)

    def close_account(self):
        self.check_open()

        if self.balance != 0:
            print("Withdraw the remaining balance before closing.")
            return

        self.closed = True
        self.history.append("Account closed")
        print("Account closed successfully.")


class SavingsAccount(Account):
    def calculate_interest(self):
        self.check_open()
        return self.balance * 6 / 100


class CurrentAccount(Account):
    def calculate_interest(self):
        self.check_open()
        return self.balance * 0 / 100


class Bank:
    def __init__(self):
        self.accounts = {}
        self.next_account_no = 1001

    def enter_text(self, message):
        while True:
            text = input(message).strip()

            if text:
                return text
            else:
                print("Error: This field cannot be empty.")

    def enter_amount(self, message, allow_zero=False):
        while True:
            try:
                amount = float(input(message))

                if amount < 0:
                    print("Error: Amount cannot be negative.")
                elif amount == 0 and not allow_zero:
                    print("Error: Amount must be greater than zero.")
                else:
                    return amount

            except ValueError:
                print("Error: Enter a valid numeric amount.")

    def create_account(self):
        name = self.enter_text("Enter customer name: ")

        print("1. Savings Account")
        print("2. Current Account")

        while True:
            account_type = input("Choose account type: ").strip()

            if account_type in ("1", "2"):
                break
            else:
                print("Error: Choose 1 or 2.")

        balance = self.enter_amount(
            "Enter opening balance: ", allow_zero=True
        )

        if account_type == "1":
            account = SavingsAccount(
                self.next_account_no, name, balance
            )
        else:
            account = CurrentAccount(
                self.next_account_no, name, balance
            )

        self.accounts[self.next_account_no] = account

        print("Account created successfully.")
        print("Your account number is:", self.next_account_no)

        self.next_account_no += 1

    def find_account(self):
        if not self.accounts:
            print("No accounts available.")
            return None

        while True:
            try:
                account_no = int(input("Enter account number: "))

                if account_no in self.accounts:
                    return self.accounts[account_no]
                else:
                    print("Error: Account not found. Try again.")

            except ValueError:
                print("Error: Enter a valid whole account number.")

    def deposit_money(self):
        account = self.find_account()

        if account is None:
            return

        try:
            account.check_open()
            amount = self.enter_amount("Enter deposit amount: ")
            account.deposit(amount)

        except AccountClosedError as error:
            print("Error:", error)

    def withdraw_money(self):
        account = self.find_account()

        if account is None:
            return

        try:
            account.check_open()
            amount = self.enter_amount("Enter withdrawal amount: ")
            account.withdraw(amount)

        except (InsufficientBalanceError, AccountClosedError) as error:
            print("Error:", error)

    def balance_enquiry(self):
        account = self.find_account()

        if account is not None:
            try:
                account.check_open()
                print("Current Balance: Rs.", round(account.balance, 2))

            except AccountClosedError as error:
                print("Error:", error)

    def interest_enquiry(self):
        account = self.find_account()

        if account is not None:
            try:
                interest = account.calculate_interest()
                print("Annual Interest: Rs.", round(interest, 2))

            except AccountClosedError as error:
                print("Error:", error)

    def display_account(self):
        account = self.find_account()

        if account is not None:
            account.display()

    def transaction_history(self):
        account = self.find_account()

        if account is not None:
            account.show_history()

    def close_account(self):
        account = self.find_account()

        if account is not None:
            try:
                account.close_account()

            except AccountClosedError as error:
                print("Error:", error)


def main():
    bank = Bank()

    while True:
        print("\n===== BANKING SYSTEM =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Balance Enquiry")
        print("5. Calculate Interest")
        print("6. Display Account")
        print("7. Transaction History")
        print("8. Close Account")
        print("9. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            bank.create_account()
        elif choice == "2":
            bank.deposit_money()
        elif choice == "3":
            bank.withdraw_money()
        elif choice == "4":
            bank.balance_enquiry()
        elif choice == "5":
            bank.interest_enquiry()
        elif choice == "6":
            bank.display_account()
        elif choice == "7":
            bank.transaction_history()
        elif choice == "8":
            bank.close_account()
        elif choice == "9":
            print("Thank you for using the Banking System.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
