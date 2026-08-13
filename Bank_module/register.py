from unittest import result

from bank import accounts
from emailsend import send_email


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

    result = send_email(
        email,
        "Welcome to Mini Bank",
        f"""
Hello {username},

Your account has been created successfully.

Account Number : {account_number}
Opening Balance : ₹{balance}

Thank you for choosing Mini Bank.
"""
    )

    print(result)

    return f"""
Registration Successful
Account Number : {account_number}
"""