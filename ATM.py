from datetime import datetime


class ATM:
    def __init__(self):
        # Sample accounts: {account_number: {'pin': pin, 'balance': balance, 'name': name, 'transactions': []}}
        self.accounts = {
            '123456': {'pin': '1234', 'balance': 1000.0, 'name': 'Michael', 'transactions': []},
            '789012': {'pin': '5678', 'balance': 2500.0, 'name': 'Ayomide', 'transactions': []},
            '345678': {'pin': '9999', 'balance': 5000.0, 'name': 'Wilson', 'transactions': []},
            '289309': {'pin': '0809', 'balance': 25000.0, 'name': 'Oluwatomisin', 'transactions': []}
        }
        self.current_account = None
        self.max_withdrawal = 1000.0  # Daily withdrawal limit

    def add_transaction(self, transaction_type, amount, description=""):
        """Add transaction to history"""
        if self.current_account:
            transaction = {
                'type': transaction_type,
                'amount': amount,
                'description': description,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'balance': self.accounts[self.current_account]['balance']
            }
            self.accounts[self.current_account]['transactions'].append(
                transaction)

    def authenticate(self, account_number, pin):
        """Authenticate user with account number and PIN"""
        if account_number in self.accounts:
            if self.accounts[account_number]['pin'] == pin:
                self.current_account = account_number
                return True
        return False

    def check_balance(self):
        """Display current balance"""
        if self.current_account:
            balance = self.accounts[self.current_account]['balance']
            print(f"\n{'='*40}")
            print(
                f"Account Holder: {self.accounts[self.current_account]['name']}")
            print(f"Account Number: {self.current_account}")
            print(f"Current Balance: ${balance:.2f}")
            print(f"{'='*40}")
            return balance
        return None

    def withdraw(self, amount):
        """Withdraw money from account"""
        if not self.current_account:
            print("Please login first!")
            return False

        if amount <= 0:
            print("Invalid amount!")
            return False

        if amount > self.max_withdrawal:
            print(
                f"Withdrawal limit exceeded! Maximum: ${self.max_withdrawal:.2f}")
            return False

        balance = self.accounts[self.current_account]['balance']

        if amount > balance:
            print("Insufficient funds!")
            return False

        self.accounts[self.current_account]['balance'] -= amount
        self.add_transaction('WITHDRAWAL', amount)

        print(f"\n{'='*40}")
        print("✓ WITHDRAWAL SUCCESSFUL")
        print(f"{'='*40}")
        print(f"Amount withdrawn: ${amount:.2f}")
        print(
            f"Remaining balance: ${self.accounts[self.current_account]['balance']:.2f}")
        print(f"{'='*40}")
        return True

    def deposit(self, amount):
        """Deposit money into account"""
        if not self.current_account:
            print("Please login first!")
            return False

        if amount <= 0:
            print("Invalid amount!")
            return False

        self.accounts[self.current_account]['balance'] += amount
        self.add_transaction('DEPOSIT', amount)

        print(f"\n{'='*40}")
        print("✓ DEPOSIT SUCCESSFUL")
        print(f"{'='*40}")
        print(f"Amount deposited: ${amount:.2f}")
        print(
            f"New balance: ${self.accounts[self.current_account]['balance']:.2f}")
        print(f"{'='*40}")
        return True

    def transfer(self, recipient_account, amount):
        """Transfer money to another account"""
        if not self.current_account:
            print("Please login first!")
            return False

        if amount <= 0:
            print("Invalid amount!")
            return False

        if recipient_account == self.current_account:
            print("Cannot transfer to the same account!")
            return False

        if recipient_account not in self.accounts:
            print("Recipient account not found!")
            return False

        balance = self.accounts[self.current_account]['balance']

        if amount > balance:
            print("Insufficient funds!")
            return False

        # Perform transfer
        self.accounts[self.current_account]['balance'] -= amount
        self.accounts[recipient_account]['balance'] += amount

        recipient_name = self.accounts[recipient_account]['name']

        self.add_transaction('TRANSFER_OUT', amount,
                             f"To: {recipient_name} ({recipient_account})")

        # Add transaction to recipient
        current = self.current_account
        self.current_account = recipient_account
        self.add_transaction(
            'TRANSFER_IN', amount, f"From: {self.accounts[current]['name']} ({current})")
        self.current_account = current

        print(f"\n{'='*40}")
        print("✓ TRANSFER SUCCESSFUL")
        print(f"{'='*40}")
        print(f"Amount transferred: ${amount:.2f}")
        print(f"To: {recipient_name} ({recipient_account})")
        print(
            f"Remaining balance: ${self.accounts[self.current_account]['balance']:.2f}")
        print(f"{'='*40}")
        return True

    def view_transaction_history(self, limit=5):
        """Display recent transaction history"""
        if not self.current_account:
            print("Please login first!")
            return

        transactions = self.accounts[self.current_account]['transactions']

        if not transactions:
            print("\nNo transaction history available.")
            return

        print(f"\n{'='*60}")
        print(
            f"TRANSACTION HISTORY - Last {min(limit, len(transactions))} transactions")
        print(f"{'='*60}")

        for trans in transactions[-limit:]:
            print(f"\nType: {trans['type']}")
            print(f"Amount: ${trans['amount']:.2f}")
            if trans['description']:
                print(f"Details: {trans['description']}")
            print(f"Date/Time: {trans['timestamp']}")
            print(f"Balance after: ${trans['balance']:.2f}")
            print("-" * 60)

    def change_pin(self, old_pin, new_pin):
        """Change account PIN"""
        if not self.current_account:
            print("Please login first!")
            return False

        if self.accounts[self.current_account]['pin'] != old_pin:
            print("Incorrect current PIN!")
            return False

        if len(new_pin) != 4 or not new_pin.isdigit():
            print("New PIN must be exactly 4 digits!")
            return False

        self.accounts[self.current_account]['pin'] = new_pin
        print("\n✓ PIN changed successfully!")
        return True

    def logout(self):
        """Logout current user"""
        if self.current_account:
            print(
                f"\nThank you, {self.accounts[self.current_account]['name']}!")
            self.current_account = None
        print("Logged out successfully.")


def main():
    atm = ATM()

    print("\n" + "="*50)
    print("     🏦 WELCOME TO Khingx BANK ATM SYSTEM 🏦")
    print("="*50)

    # Login
    while True:
        print("\n--- LOGIN ---")
        account = input("Enter account number (or 'exit' to quit): ").strip()

        if account.lower() == 'exit':
            print("\nThank you for using Khingx Bank ATM!")
            return

        pin = input("Enter PIN: ").strip()

        if atm.authenticate(account, pin):
            print(
                f"\n✓ Login successful! Welcome, {atm.accounts[account]['name']}!")
            break
        else:
            print("\n✗ Invalid account number or PIN. Please try again.")

    # Main menu
    while True:
        print("\n" + "="*50)
        print("                   MAIN MENU")
        print("="*50)
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Transfer Money")
        print("5. Transaction History")
        print("6. Change PIN")
        print("7. Logout")
        print("="*50)

        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == '1':
            atm.check_balance()

        elif choice == '2':
            try:
                amount = float(input("Enter amount to withdraw: $"))
                atm.withdraw(amount)
            except ValueError:
                print("✗ Invalid amount entered!")

        elif choice == '3':
            try:
                amount = float(input("Enter amount to deposit: $"))
                atm.deposit(amount)
            except ValueError:
                print("✗ Invalid amount entered!")

        elif choice == '4':
            recipient = input("Enter recipient account number: ").strip()
            try:
                amount = float(input("Enter amount to transfer: $"))
                atm.transfer(recipient, amount)
            except ValueError:
                print("✗ Invalid amount entered!")

        elif choice == '5':
            try:
                limit = input(
                    "Enter number of transactions to view (default 5): ").strip()
                limit = int(limit) if limit else 5
                atm.view_transaction_history(limit)
            except ValueError:
                atm.view_transaction_history(5)

        elif choice == '6':
            old_pin = input("Enter current PIN: ").strip()
            new_pin = input("Enter new PIN (4 digits): ").strip()
            confirm_pin = input("Confirm new PIN: ").strip()

            if new_pin != confirm_pin:
                print("✗ PINs do not match!")
            else:
                atm.change_pin(old_pin, new_pin)

        elif choice == '7':
            atm.logout()
            print("\nThank you for using Khingx Bank ATM!")
            break

        else:
            print("✗ Invalid choice! Please select 1-7.")
