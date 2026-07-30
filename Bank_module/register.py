from bank import accounts

def register(username, email, balance, password):
    if len(accounts) == 0:
        account_number = 1001
    else:
        account_number = max(accounts.keys()) + 1

    accounts[account_number] = {
        "username": username,
        "email": email,
        "password": password,
        "balance": balance,
        "statement": [
            f"Account Created with ₹{balance}"
        ]
    }

    return f"""
Registration Successful
Account Number : {account_number}
"""