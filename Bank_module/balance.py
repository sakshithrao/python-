from bank import accounts


def get_balance(account):

    return f"""
=====================
Available Balance
=====================
₹{accounts[account]["balance"]}
"""