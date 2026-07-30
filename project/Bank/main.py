# Data base
"""
users ={
        Account :{
                'name':user name,
                'gmail':user gmail,
                'balance':5000,
                'password':password
            }
        }
"""
users={
        1001:{'name':"sakshith",'gmail':"sakshithrao85@gmail.com",'balance':5000,'password':'1001'},
        1002:{'name':"sairam",'gmail':"sairam5@gmail.com",'balance':1000,'password':'1002'}
        }



# Register function
def register(username:str,gmail:str,balance:int,password:str)-> int:
    print("user in register page")

# login function
def login(account:int,password:str)-> bool:
    if account in users:
        if users [account]['password'] == password:
            return True
        return False
    return False

# get balance
def get_balance(account:int)-> str:
    curr_balance = users[account]['balance']
    return f"Current Balance is:{curr_balance}"

# withdraw function
def withdraw(account:int,withdraw_amount:int)-> str:
    curr_balance = users[account]['balance']
    if curr_balance >= withdraw_amount:
        users[account]['balance'] -= withdraw_amount
        return f"{withdraw_amount} withdraw successful and\
                        current balance is :{users[account]['balance']}"
    return "Insufficient Amount" 

# deposit function
def deposit(account:int,deposit_amount:int)-> str:
    users[account]['balance'] += deposit_amount
    return f"{deposit_amount} deposite successful and\
                            current balance is :{users[account]['balance']}"

# transfer function
def transfer(sender_account:int,receiver_account:int,transfer_amount:int)-> str:
    if sender_account == receiver_account:
        return "Cannot transfer to the same account"

    if receiver_account not in users:
        return "Receiver account does not exist"

    if users[sender_account]['balance'] >= transfer_amount:
        users[sender_account]['balance'] -= transfer_amount
        users[receiver_account]['balance'] += transfer_amount

        return f"{transfer_amount} transferred successfully to account {receiver_account} and\
                current balance is :{users[sender_account]['balance']}"

    return "Insufficient Amount"

# mini statement function
def mini_statement(account:int):
    print("user in ministatement page")

# logout function
def logout():
    print("Buy Buy buddy , see you later")
    exit()


# main
if __name__=="__main__":
    print("welcome to the Mini Bank")
    print("1.login \n 2. Register")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        # call login function
        account = int(input("Enter your account number: "))
        password = input("Enter your password: ")
        login_val = login(account = account,password = password)
        while login_val:

            print("1. Get Balance \n 2. Withdraw \n 3. Deposit \n 4. Transfer \n 5. Mini Statement \n 6. Logout")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                # call balance function
                print(get_balance(account = account))
            elif choice == 2:
                amount = int(input("Enter withdraw amount:"))
                print(withdraw(account = account,withdraw_amount = amount))
            elif choice == 3:
                amount = int(input("Enter deposit amount:"))
                print(deposit(account = account,deposit_amount = amount))
            elif choice == 4:
                receiver_account = int(input("Enter receiver account number:"))
                amount = int(input("Enter transfer amount:"))
                print(transfer(sender_account = account,receiver_account = receiver_account,transfer_amount = amount))
            elif choice == 5:
                print(mini_statement(account = account))
            elif choice == 6:
                print(logout())
            else:
                print("Select your choice in between 1 to 6")

        else:
            print("Invalid login credevtials")
    elif choice == 2:
        username = input("Enter user name:")
        email = input("Enter user mail id")
        initial_deposite = int(input("Enter the initial deposite amount:"))
        password = input("Enter your new password:")
        print(register(username=username,
                    email=email,
                    balance=initial_deposite,
                    password=password))
    else:
        print("Invalid choice,please select 1 or 2")