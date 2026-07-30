import addition
import subtraction
import multiplication
import division


def menu():
    print("\n===== SMALL CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


if __name__ == "__main__":

    print("Welcome to Small Calculator")

    while True:

        menu()

        choice = int(input("Enter your choice: "))

        if choice == 5:
            print("Thank you for using Small Calculator.")
            break

        if choice not in [1, 2, 3, 4]:
            print("Invalid Choice")
            continue

        a, b = map(int, input("Enter two numbers separated by space: ").split())

        if choice == 1:
            result = addition.add(a, b)
            print(f"{a} + {b} = {result}")

        elif choice == 2:
            result = subtraction.sub(a, b)
            print(f"{a} - {b} = {result}")

        elif choice == 3:
            result = multiplication.mul(a, b)
            print(f"{a} × {b} = {result}")

        elif choice == 4:
            result = division.div(a, b)
            print(f"{a} ÷ {b} = {result}")


            