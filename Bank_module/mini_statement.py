from bank import accounts


def mini_statement(account):

    print("\n========== MINI STATEMENT ==========")

    for transaction in accounts[account]["statement"]:
        print(transaction)

    return ""