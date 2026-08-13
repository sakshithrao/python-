from helper import print_heading

from product import (
    add_product,
    view_products,
    update_product,
    delete_product
)

from inventory import (
    add_stock,
    reduce_stock,
    view_stock,
    low_stock
)

from purchase import (
    purchase_product,
    view_purchase_history
)

from sales import (
    sell_product,
    view_sales_history
)

from search import (
    search_by_id,
    search_by_name,
    search_by_category
)

from reports import (
    inventory_report,
    purchase_report,
    sales_report,
    profit_report
)


def product_menu():

    while True:

        print_heading("PRODUCT MANAGEMENT")

        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            update_product()

        elif choice == "4":
            delete_product()

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


def inventory_menu():

    while True:

        print_heading("INVENTORY MANAGEMENT")

        print("1. Add Stock")
        print("2. Reduce Stock")
        print("3. View Stock")
        print("4. Low Stock")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_stock()

        elif choice == "2":
            reduce_stock()

        elif choice == "3":
            view_stock()

        elif choice == "4":
            low_stock()

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


def purchase_menu():

    while True:

        print_heading("PURCHASE MANAGEMENT")

        print("1. Purchase Product")
        print("2. Purchase History")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            purchase_product()

        elif choice == "2":
            view_purchase_history()

        elif choice == "3":
            break

        else:
            print("Invalid choice.")


def sales_menu():

    while True:

        print_heading("SALES MANAGEMENT")

        print("1. Sell Product")
        print("2. Sales History")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            sell_product()

        elif choice == "2":
            view_sales_history()

        elif choice == "3":
            break

        else:
            print("Invalid choice.")


def search_menu():

    while True:

        print_heading("SEARCH PRODUCT")

        print("1. Search by Product ID")
        print("2. Search by Product Name")
        print("3. Search by Category")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            search_by_id()

        elif choice == "2":
            search_by_name()

        elif choice == "3":
            search_by_category()

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


def reports_menu():

    while True:

        print_heading("REPORTS")

        print("1. Inventory Report")
        print("2. Purchase Report")
        print("3. Sales Report")
        print("4. Profit Report")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            inventory_report()

        elif choice == "2":
            purchase_report()

        elif choice == "3":
            sales_report()

        elif choice == "4":
            profit_report()

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


def main():

    while True:

        print_heading("SMART INVENTORY MANAGEMENT SYSTEM")

        print("1. Product Management")
        print("2. Inventory Management")
        print("3. Purchase Management")
        print("4. Sales Management")
        print("5. Search Product")
        print("6. Reports")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            product_menu()

        elif choice == "2":
            inventory_menu()

        elif choice == "3":
            purchase_menu()

        elif choice == "4":
            sales_menu()

        elif choice == "5":
            search_menu()

        elif choice == "6":
            reports_menu()

        elif choice == "7":
            print("Thank you for using Smart Inventory Management System.")
            break

        else:
            print("Invalid choice.")


main()