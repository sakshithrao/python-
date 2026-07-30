from bank import accounts


def transfer(sender_account,
             receiver_account,
             amount):

    if receiver_account not in accounts:
        return "Receiver Account Not Found"

    if amount <= 0:
        return "Invalid Amount"

    if amount > accounts[sender_account]["balance"]:
        return "Insufficient Balance"

    accounts[sender_account]["balance"] -= amount

    accounts[receiver_account]["balance"] += amount

    accounts[sender_account]["statement"].append(
        f"Transferred ₹{amount} to Account {receiver_account}"
    )

    accounts[receiver_account]["statement"].append(
        f"Received ₹{amount} from Account {sender_account}"
    )

    return "Transfer Successful"