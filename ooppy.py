class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' Balance = ${self.balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("\nDeposit amount must be positive.")
            return
        self.balance += amount
        print(f"\nDeposit of ${amount:.2f} complete.")
        self.getBalance()

    def availableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.availableTransaction(amount)
            self.balance -= amount
            print(f"\nWithdrawal of ${amount:.2f} complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

    def transfer(self, amount, account):
        try:
            print('\n*******\n\nBeginning transfer')
            self.availableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete! Check! ✅')
        except BalanceException as e:
            print(f'\nTransfer failed due to balance error: {e}')
        except Exception as e:
            print(f'\nTransfer failedi: {e}')
class InterestRewardsAcc(BankAccount):
    def deposit(self, amount):
        if amount <= 0:
            print("\nDeposit amount must be positive.")
            return
        # Add 5% bonus interest
        interest_amount = amount * 1.05
        self.balance += interest_amount
        print(f"\nDeposit of ${amount:.2f} + 5% interest complete.")
        self.getBalance()

class SavingsAcct(InterestRewardsAcc):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.availableTransaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print("\nWithdrawal completed with $5 fee.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdrawal Error: {error}")

