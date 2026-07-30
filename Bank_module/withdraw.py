from bank import accounts


def withdraw(account, amount):

    if amount <= 0:
        return "Invalid Amount"

    if amount > accounts[account]["balance"]:
        return "Insufficient Balance"

    accounts[account]["balance"] -= amount

    accounts[account]["statement"].append(
        f"Withdraw ₹{amount}"
    )

    return f"""
Withdraw Successful

Current Balance : ₹{accounts[account]["balance"]}
"""