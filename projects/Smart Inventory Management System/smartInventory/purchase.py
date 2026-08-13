from database import read_data, write_data
from config import PRODUCTS_FILE, PURCHASES_FILE
from helper import generate_product_id, get_current_date, print_heading
from validation import validate_price, validate_quantity


def purchase_product():

    print_heading("PURCHASE PRODUCT")

    product_id = input("Enter product ID: ")

    products = read_data(PRODUCTS_FILE)

    for product in products:

        if product["product_id"] == product_id:

            quantity = input("Enter quantity purchased: ")

            if not validate_quantity(quantity):
                print("Invalid quantity.")
                return

            purchase_price = input("Enter purchase price per item: ")

            if not validate_price(purchase_price):
                print("Invalid purchase price.")
                return

            supplier = input("Enter supplier name: ")

            if supplier.strip() == "":
                print("Supplier name cannot be empty.")
                return

            quantity = int(quantity)
            purchase_price = float(purchase_price)

            total_amount = quantity * purchase_price

            product["quantity"] += quantity

            purchases = read_data(PURCHASES_FILE)

            purchase = {
                "purchase_id": generate_product_id(),
                "product_id": product["product_id"],
                "product_name": product["name"],
                "supplier": supplier,
                "quantity": quantity,
                "purchase_price": purchase_price,
                "total_amount": total_amount,
                "purchase_date": get_current_date()
            }

            purchases.append(purchase)

            write_data(PRODUCTS_FILE, products)
            write_data(PURCHASES_FILE, purchases)

            print("\nPurchase recorded successfully.")
            print("Total amount:", total_amount)
            print("Current stock:", product["quantity"])

            return

    print("Product not found.")


def view_purchase_history():

    print_heading("PURCHASE HISTORY")

    purchases = read_data(PURCHASES_FILE)

    if not purchases:
        print("No purchase records found.")
        return

    for purchase in purchases:

        print("-" * 50)

        print("Purchase ID    :", purchase["purchase_id"])
        print("Product ID     :", purchase["product_id"])
        print("Product Name   :", purchase["product_name"])
        print("Supplier       :", purchase["supplier"])
        print("Quantity       :", purchase["quantity"])
        print("Purchase Price :", purchase["purchase_price"])
        print("Total Amount   :", purchase["total_amount"])
        print("Purchase Date  :", purchase["purchase_date"])

    print("-" * 50)