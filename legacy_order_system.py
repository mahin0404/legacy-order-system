
"""Order calculator for SREE practical.
All prices are in PKR. Not for real payment processing.
"""

# Named constants
STUDENT_DISCOUNT = 0.10
STAFF_DISCOUNT = 0.05

EXPRESS_DELIVERY_FEE = 250
STANDARD_DELIVERY_FEE = 100


def calculate_subtotal(items):
    """Calculate item costs and reject negative prices or quantities."""
    subtotal = 0

    for item in items:
        price = item['price']
        quantity = item['qty']

        if price < 0:
            raise ValueError("Price cannot be negative")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        subtotal = subtotal + price * quantity

    return subtotal


def calculate_discount(subtotal, customer_type):
    """Calculate the discount for the customer type."""
    if customer_type == 'student':
        return subtotal * STUDENT_DISCOUNT
    elif customer_type == 'staff':
        return subtotal * STAFF_DISCOUNT

    return 0


def calculate_delivery_fee(delivery):
    """Return the delivery fee."""
    if delivery == 'express':
        return EXPRESS_DELIVERY_FEE
    elif delivery == 'standard':
        return STANDARD_DELIVERY_FEE

    return 0


def order_total(items, customer_type, delivery):
    """Calculate the final order total."""
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal, customer_type)
    delivery_fee = calculate_delivery_fee(delivery)

    total = subtotal - discount + delivery_fee

    return round(total, 2)


def print_receipt(items, customer_type, delivery):
    """Create a text receipt for the order."""
    amount = order_total(items, customer_type, delivery)

    result = 'ORDER RECEIPT\n'

    for item in items:
        item_total = item['price'] * item['qty']
        result += (
            str(item['qty']) + ' x ' + item['name']
            + ' = ' + str(item_total) + '\n'
        )

    result += 'Customer: ' + customer_type + '\n'
    result += 'Delivery: ' + delivery + '\n'
    result += 'Total: ' + str(amount)

    return result


if __name__ == '__main__':
    sample = [
        {'name': 'Notebook', 'category': 'book',
         'price': 300, 'qty': 2},
        {'name': 'USB Drive', 'category': 'electronics',
         'price': 800, 'qty': 1},
    ]

    print(print_receipt(sample, 'student', 'standard'))
