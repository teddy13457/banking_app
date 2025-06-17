class SavingsAccount:
    def __init__(self, account_number, initial_balance, interest_rate):
        self.account_number = account_number
        self.balance = initial_balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Added ${interest:.2f} interest. New balance: ${self.balance:.2f}")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

# Example usage:
account = SavingsAccount("123456789", 1000, 2)
account.check_balance()
account.deposit(500)
account.withdraw(200)
account.add_interest()
account.check_balance()

import streamlit as st

# Current Account Class
class CurrentAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ₦{amount} successfully."
        else:
            return "Enter a valid deposit amount."

    def withdraw(self, amount):
        if amount <= 0:
            return "Enter a valid withdrawal amount."
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal of ₦{amount} successful."
        else:
            return "Insufficient funds."

    def get_balance(self):
        return self.balance

# Create a CurrentAccount instance
current_account = CurrentAccount()

# Streamlit UI
st.title("🏦 CSC104 Current Account System")
st.header("🔁 Current Account Operations")

# Display current balance
st.write(f"💼 Current Balance: ₦{current_account.get_balance():,.2f}")

# Choose action
action = st.radio("Choose an action", ["Deposit", "Withdraw"])

# Amount input
amount = st.number_input("Enter amount", min_value=0, step=500)

# Action buttons
if st.button("Submit"):
    if action == "Deposit":
        result = current_account.deposit(amount)
        st.success(result)
    elif action == "Withdraw":
        result = current_account.withdraw(amount)
        if "successful" in result:
            st.success(result)
        else:
            st.error(result)

import tkinter as tk
from tkinter import messagebox

class BankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank App")

        # Initial balances for accounts
        self.balances = {
            "Savings": 1000.0,
            "Current": 2000.0
        }

        # Account selection
        self.account_var = tk.StringVar(value="Savings")
        tk.Label(root, text="Select Account:").grid(row=0, column=0, pady=10)
        tk.Radiobutton(root, text="Savings", variable=self.account_var, value="Savings").grid(row=0, column=1)
        tk.Radiobutton(root, text="Current", variable=self.account_var, value="Current").grid(row=0, column=2)

        # Withdrawal amount entry
        tk.Label(root, text="Withdrawal Amount:").grid(row=1, column=0, pady=10)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=1, column=1, columnspan=2)

        # Withdraw button
        withdraw_btn = tk.Button(root, text="Withdraw", command=self.withdraw)
        withdraw_btn.grid(row=2, column=0, columnspan=3, pady=10)

        # Balance display
        self.balance_label = tk.Label(root, text="")
        self.balance_label.grid(row=3, column=0, columnspan=3)
        self.update_balance()

    def update_balance(self):
        account = self.account_var.get()
        balance = self.balances[account]
        self.balance_label.config(text=f"{account} Account Balance: ${balance:.2f}")

    def withdraw(self):
        account = self.account_var.get()
        amount_str = self.amount_entry.get()
        try:
            amount = float(amount_str)
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            if amount > self.balances[account]:
                messagebox.showerror("Error", "Insufficient funds!")
            else:
                self.balances[account] -= amount
                messagebox.showinfo("Success", f"${amount:.2f} withdrawn from {account} account.")
                self.update_balance()
                self.amount_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()