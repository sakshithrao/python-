def validate_name(name):

    if name.strip() == "":
        return False

    return True


def validate_price(price):

    try:
        price = float(price)

        if price < 0:
            return False

        return True

    except ValueError:
        return False


def validate_quantity(quantity):

    try:
        quantity = int(quantity)

        if quantity < 0:
            return False

        return True

    except ValueError:
        return False