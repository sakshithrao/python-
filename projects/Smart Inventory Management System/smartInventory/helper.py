from datetime import datetime
import uuid


def generate_product_id():
    product_id = uuid.uuid4().hex[:8].upper()
    return "PROD-" + product_id


def get_current_date():
    return datetime.now().strftime("%d-%m-%Y")


def print_heading(title):
    print()
    print("=" * 50)
    print(title)
    print("=" * 50)