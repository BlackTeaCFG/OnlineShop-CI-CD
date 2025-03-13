def calculate_order_total(items):
    """Calculate the total price of items in the order."""
    return sum(item['price'] * item['quantity'] for item in items)

def apply_discount(total, discount_percent):
    """Apply discount to the order total."""
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")
    return total * (1 - discount_percent / 100)