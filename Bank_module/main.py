import register
import login
import balance
import deposit
import withdraw
import transfer
import mini_statement
import logout

if __name__ == "__main__":

    print("========== MINI BANK ==========")

    while True:

        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = int(input("Enter Choice : "))

        if choice == 1:

            username = input("Username : ")

            email = input("Email : ")

            amount = int(input("Initial Deposit : "))

            password = input("Create Password : ")

            print(register.register(
                username,
                email,
                amount,
                password
            ))

        elif choice == 2:

            account = int(input("Account Number : "))

            password = input("Password : ")

            if login.login(account, password):

                print("\nLogin Successful")

                while True:

                    print("\n========== MENU ==========")
                    print("1. Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Transfer")
                    print("5. Mini Statement")
                    print("6. Logout")

                    option = int(input("Enter Choice : "))

                    if option == 1:

                        print(balance.get_balance(account))

                    elif option == 2:

                        amount = int(input("Deposit Amount : "))

                        print(deposit.deposit(account,
                                                amount))

                    elif option == 3:

                        amount = int(input("Withdraw Amount : "))

                        print(withdraw.withdraw(account,
                                                amount))

                    elif option == 4:

                        receiver = int(input("Receiver Account : "))

                        amount = int(input("Transfer Amount : "))

                        print(
                            transfer.transfer(
                                account,
                                receiver,
                                amount
                            )
                        )

                    elif option == 5:

                        mini_statement.mini_statement(account)

                    elif option == 6:

                        print(logout.logout())
                        break

                    else:

                        print("Invalid Choice")

            else:

                print("Invalid Account Number or Password")

        elif choice == 3:

            print("Thank You for Using Mini Bank")
            break

        else:

            print("Invalid Choice")