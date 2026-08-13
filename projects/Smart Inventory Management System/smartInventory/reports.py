from database import read_data
from config import PRODUCTS_FILE, PURCHASES_FILE, SALES_FILE
from helper import print_heading


def inventory_report():

    print_heading("INVENTORY REPORT")

    products = read_data(PRODUCTS_FILE)

    if not products:
        print("No products found.")
        return

    total_products = len(products)
    total_stock = 0
    low_stock = 0
    out_of_stock = 0

    for product in products:

        total_stock += product["quantity"]

        if product["quantity"] == 0:
            out_of_stock += 1

        elif product["quantity"] <= 5:
            low_stock += 1

    print("Total Products :", total_products)
    print("Total Stock    :", total_stock)
    print("Low Stock      :", low_stock)
    print("Out of Stock   :", out_of_stock)


def purchase_report():

    print_heading("PURCHASE REPORT")

    purchases = read_data(PURCHASES_FILE)

    if not purchases:
        print("No purchase records found.")
        return

    total_purchases = len(purchases)
    total_quantity = 0
    total_amount = 0

    for purchase in purchases:

        total_quantity += purchase["quantity"]
        total_amount += purchase["total_amount"]

    print("Total Purchases :", total_purchases)
    print("Total Quantity  :", total_quantity)
    print("Total Amount    :", total_amount)


def sales_report():

    print_heading("SALES REPORT")

    sales = read_data(SALES_FILE)

    if not sales:
        print("No sales records found.")
        return

    total_sales = len(sales)
    total_quantity = 0
    total_amount = 0

    for sale in sales:

        total_quantity += sale["quantity"]
        total_amount += sale["total_amount"]

    print("Total Sales    :", total_sales)
    print("Total Quantity :", total_quantity)
    print("Total Amount   :", total_amount)


def profit_report():

    print_heading("PROFIT REPORT")

    sales = read_data(SALES_FILE)

    if not sales:
        print("No sales records found.")
        return

    total_profit = 0

    for sale in sales:

        purchase_price = sale.get("purchase_price", 0)
        selling_price = sale["selling_price"]
        quantity = sale["quantity"]

        profit = (selling_price - purchase_price) * quantity

        total_profit += profit

    print("Total Profit :", total_profit)
        