from bank import accounts


def login(account, password):

    if account not in accounts:
        return False

    if accounts[account]["password"] == password:
        return True

    return False