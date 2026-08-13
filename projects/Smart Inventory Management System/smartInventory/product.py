from database import read_data, write_data
from config import PRODUCTS_FILE
from helper import generate_product_id, print_heading
from validation import validate_name, validate_price, validate_quantity


def add_product():

    print_heading("ADD PRODUCT")

    name = input("Enter product name: ")

    if not validate_name(name):
        print("Product name cannot be empty.")
        return

    category = input("Enter category: ")

    if not validate_name(category):
        print("Category cannot be empty.")
        return

    purchase_price = input("Enter purchase price: ")

    if not validate_price(purchase_price):
        print("Invalid purchase price.")
        return

    selling_price = input("Enter selling price: ")

    if not validate_price(selling_price):
        print("Invalid selling price.")
        return

    quantity = input("Enter quantity: ")

    if not validate_quantity(quantity):
        print("Invalid quantity.")
        return

    products = read_data(PRODUCTS_FILE)

    product = {
        "product_id": generate_product_id(),
        "name": name,
        "category": category,
        "purchase_price": float(purchase_price),
        "selling_price": float(selling_price),
        "quantity": int(quantity)
    }

    products.append(product)

    write_data(PRODUCTS_FILE, products)

    print("\nProduct added successfully.")


def view_products():

    print_heading("PRODUCT LIST")

    products = read_data(PRODUCTS_FILE)

    if not products:
        print("No products found.")
        return

    for product in products:

        print("-" * 50)
        print("Product ID     :", product["product_id"])
        print("Name           :", product["name"])
        print("Category       :", product["category"])
        print("Purchase Price :", product["purchase_price"])
        print("Selling Price  :", product["selling_price"])
        print("Quantity       :", product["quantity"])

    print("-" * 50)


def update_product():

    print_heading("UPDATE PRODUCT")

    product_id = input("Enter product ID: ")

    products = read_data(PRODUCTS_FILE)

    for product in products:

        if product["product_id"] == product_id:

            print("\nLeave the field empty to keep the old value.")

            name = input("Enter new name: ")

            if name:
                if validate_name(name):
                    product["name"] = name
                else:
                    print("Invalid name.")
                    return

            category = input("Enter new category: ")

            if category:
                if validate_name(category):
                    product["category"] = category
                else:
                    print("Invalid category.")
                    return

            purchase_price = input("Enter new purchase price: ")

            if purchase_price:

                if validate_price(purchase_price):
                    product["purchase_price"] = float(purchase_price)
                else:
                    print("Invalid purchase price.")
                    return

            selling_price = input("Enter new selling price: ")

            if selling_price:

                if validate_price(selling_price):
                    product["selling_price"] = float(selling_price)
                else:
                    print("Invalid selling price.")
                    return

            quantity = input("Enter new quantity: ")

            if quantity:

                if validate_quantity(quantity):
                    product["quantity"] = int(quantity)
                else:
                    print("Invalid quantity.")
                    return

            write_data(PRODUCTS_FILE, products)

            print("\nProduct updated successfully.")
            return

    print("Product not found.")


def delete_product():

    print_heading("DELETE PRODUCT")

    product_id = input("Enter product ID: ")

    products = read_data(PRODUCTS_FILE)

    for product in products:

        if product["product_id"] == product_id:

            products.remove(product)

            write_data(PRODUCTS_FILE, products)

            print("\nProduct deleted successfully.")
            return

    print("Product not found.")