from database import read_data, write_data
from config import PRODUCTS_FILE, LOW_STOCK_LIMIT
from helper import print_heading
from validation import validate_quantity


def add_stock():

    print_heading("ADD STOCK")

    product_id = input("Enter product ID: ")

    products = read_data(PRODUCTS_FILE)

    for product in products:

        if product["product_id"] == product_id:

            quantity = input("Enter quantity to add: ")

            if not validate_quantity(quantity):
                print("Invalid quantity.")
                return

            quantity = int(quantity)

            product["quantity"] += quantity

            write_data(PRODUCTS_FILE, products)

            print("\nStock added successfully.")
            print("Current stock:", product["quantity"])

            return

    print("Product not found.")


def reduce_stock():

    print_heading("REDUCE STOCK")

    product_id = input("Enter product ID: ")

    products = read_data(PRODUCTS_FILE)

    for product in products:

        if product["product_id"] == product_id:

            quantity = input("Enter quantity to remove: ")

            if not validate_quantity(quantity):
                print("Invalid quantity.")
                return

            quantity = int(quantity)

            if quantity > product["quantity"]:
                print("Not enough stock available.")
                return

            product["quantity"] -= quantity

            write_data(PRODUCTS_FILE, products)

            print("\nStock reduced successfully.")
            print("Current stock:", product["quantity"])

            return

    print("Product not found.")


def view_stock():

    print_heading("CURRENT STOCK")

    products = read_data(PRODUCTS_FILE)

    if not products:
        print("No products found.")
        return

    for product in products:

        print("-" * 40)

        print("Product ID :", product["product_id"])
        print("Name       :", product["name"])
        print("Category   :", product["category"])
        print("Stock      :", product["quantity"])

    print("-" * 40)


def low_stock():

    print_heading("LOW STOCK PRODUCTS")

    products = read_data(PRODUCTS_FILE)

    found = False

    for product in products:

        if product["quantity"] <= LOW_STOCK_LIMIT:

            print("-" * 40)

            print("Product ID :", product["product_id"])
            print("Name       :", product["name"])
            print("Stock      :", product["quantity"])

            found = True

    if not found:
        print("No low stock products.")