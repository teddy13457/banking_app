import streamlit as st


# Current Account Class
class CurrentAccount:
    def _init_(self):
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


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
