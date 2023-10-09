#!/usr/bin/env python
# coding: utf-8

# In[9]:


class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.balance

class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=100):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
        else:
            print("Withdrawal exceeds overdraft limit.")

class SavingsAccount(Account):
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds for withdrawal.")

class BusinessAccount(Account):
    def __init__(self, account_number, balance=0, credit_limit=1000):
        super().__init__(account_number, balance)
        self.credit_limit = credit_limit

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= -self.credit_limit:
            self.balance -= amount
        else:
            print("Withdrawal exceeds credit limit.")

def create_account():
    account_type = input("Enter account type (Checking/Savings/Business): ").capitalize()
    account_number = input("Enter account number: ")

    if account_type == "Checking":
        return CheckingAccount(account_number)
    elif account_type == "Savings":
        return SavingsAccount(account_number)
    elif account_type == "Business":
        return BusinessAccount(account_number)
    else:
        print("Invalid account type. Please choose Checking, Savings, or Business.")
        return None

def atm_interface(account):
    while True:
        print("\nATM Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = float(input("Enter the deposit amount: "))
            account.deposit(amount)
            print("Deposit successful.")

        elif choice == '2':
            amount = float(input("Enter the withdrawal amount: "))
            account.withdraw(amount)
            print("Withdrawal successful.")

        elif choice == '3':
            print(f"Current Balance: ${account.get_balance()}")

        elif choice == '4':
            print("Exiting ATM. Have a nice day!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    account = create_account()

    if account:
        print("\nWelcome to the Bank Account Manager!")
        atm_interface(account)


# In[ ]:




