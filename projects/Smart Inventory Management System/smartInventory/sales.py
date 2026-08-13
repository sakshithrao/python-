from database import read_data, write_data
from config import PRODUCTS_FILE, SALES_FILE
from helper import generate_product_id, get_current_date, print_heading
from validation import validate_quantity


def sell_product():

    print_heading("SELL PRODUCT")

    product_id = input("Enter product ID: ")

    products = read_data(PRODUCTS_FILE)

    for product in products:

        if product["product_id"] == product_id:

            quantity = input("Enter quantity to sell: ")

            if not validate_quantity(quantity):
                print("Invalid quantity.")
                return

            quantity = int(quantity)

            if quantity == 0:
                print("Quantity should be greater than zero.")
                return

            if quantity > product["quantity"]:
                print("Not enough stock available.")
                return

            total_amount = quantity * product["selling_price"]

            product["quantity"] -= quantity

            sales = read_data(SALES_FILE)

            sale = {
                "sale_id": generate_product_id(),
                "product_id": product["product_id"],
                "product_name": product["name"],
                "quantity": quantity,
                "selling_price": product["selling_price"],
                "total_amount": total_amount,
                "sale_date": get_current_date()
            }

            sales.append(sale)

            write_data(PRODUCTS_FILE, products)
            write_data(SALES_FILE, sales)

            print("\nSale completed successfully.")
            print("Product :", product["name"])
            print("Quantity :", quantity)
            print("Total amount :", total_amount)
            print("Remaining stock :", product["quantity"])

            return

    print("Product not found.")


def view_sales_history():

    print_heading("SALES HISTORY")

    sales = read_data(SALES_FILE)

    if not sales:
        print("No sales records found.")
        return

    for sale in sales:

        print("-" * 50)

        print("Sale ID        :", sale["sale_id"])
        print("Product ID     :", sale["product_id"])
        print("Product Name   :", sale["product_name"])
        print("Quantity       :", sale["quantity"])
        print("Selling Price  :", sale["selling_price"])
        print("Total Amount   :", sale["total_amount"])
        print("Sale Date      :", sale["sale_date"])

    print("-" * 50)