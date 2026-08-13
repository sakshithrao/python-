from database import read_data
from config import PRODUCTS_FILE
from helper import print_heading


def display_product(product):

    print("-" * 50)
    print("Product ID     :", product["product_id"])
    print("Name           :", product["name"])
    print("Category       :", product["category"])
    print("Purchase Price :", product["purchase_price"])
    print("Selling Price  :", product["selling_price"])
    print("Quantity       :", product["quantity"])


def search_by_id():

    print_heading("SEARCH BY PRODUCT ID")

    product_id = input("Enter product ID: ")

    products = read_data(PRODUCTS_FILE)

    for product in products:

        if product["product_id"] == product_id:
            display_product(product)
            return

    print("Product not found.")


def search_by_name():

    print_heading("SEARCH BY PRODUCT NAME")

    name = input("Enter product name: ").lower()

    products = read_data(PRODUCTS_FILE)

    found = False

    for product in products:

        if name in product["name"].lower():
            display_product(product)
            found = True

    if not found:
        print("Product not found.")


def search_by_category():

    print_heading("SEARCH BY CATEGORY")

    category = input("Enter category: ").lower()

    products = read_data(PRODUCTS_FILE)

    found = False

    for product in products:

        if category in product["category"].lower():
            display_product(product)
            found = True

    if not found:
        print("No products found in this category.")