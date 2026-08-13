# Smart Inventory Management System

## About the Project

Smart Inventory Management System is a console-based Python project used to manage products and their stock.

The project allows us to add, view, update and delete products. It also manages stock, records purchases and sales, searches for products and generates basic reports.

The main purpose of this project is to practice Python programming by building a real-world application using simple and understandable logic.

## Features

- Add product
- View products
- Update product
- Delete product
- Add stock
- Reduce stock
- View current stock
- Check low-stock products
- Record purchases
- View purchase history
- Sell products
- View sales history
- Search products by ID
- Search products by name
- Search products by category
- Generate inventory report
- Generate purchase report
- Generate sales report
- Generate profit report

## Technologies Used

- Python
- JSON
- File Handling
- Functions
- Exception Handling
- Modules

## Python Built-in Modules Used

- json
- datetime
- uuid

No third-party libraries are used in this project.

## Project Structure

```text
smartInventory/
│
├── data/
│   ├── categories.json
│   ├── products.json
│   ├── purchases.json
│   └── sales.json
│
├── logs/
│   └── inventory.log
│
├── config.py
├── database.py
├── helper.py
├── validation.py
├── product.py
├── inventory.py
├── purchase.py
├── sales.py
├── search.py
├── reports.py
├── main.py
└── README.md