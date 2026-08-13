from bank import accounts
from emailsend import send_email



def deposit(account, amount):

    if amount <= 0:
        return "Invalid Amount"

    accounts[account]["balance"] += amount

    accounts[account]["statement"].append(
        f"Deposited ₹{amount}"
    )

    return f"""
Deposit Successful

Current Balance : ₹{accounts[account]["balance"]}
"""