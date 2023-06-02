def calculate_tax(state_code, item_price):
    tax_rate = 0.0
    if state_code == "UT":
        tax_rate = 0.0358
    elif state_code == "NY":
        tax_rate = 0.0578

    return item_price * tax_rate


def calculate_discount(order_value):
    discount_rate = 0.0
    if order_value >= 50000:
        discount_rate = 0.10
    elif order_value >= 10000:
        discount_rate = 0.07
    elif order_value >= 5000:
        discount_rate = 0.05
    elif order_value >= 1000:
        discount_rate = 0.03

    return discount_rate


def calculate_order(count_of_items, item_price, state_code):
    total_items_price = count_of_items * item_price
    tax = calculate_tax(state_code, total_items_price)
    order_value = total_items_price + tax
    discount_rate = calculate_discount(order_value)
    discount = order_value * discount_rate
    total_order_value = order_value - discount

    return total_items_price, discount, total_order_value

# Example usage:
count_of_items = int(input("Enter the count of items: "))
item_price = float(input("Enter the item price: "))
state_code = input("Enter the state code for tax purpose (UT/NY): ")

items_price, discount, total_order_value = calculate_order(count_of_items, item_price, state_code)

print("Items Price:", items_price)
print("Discount Applied:", discount)
print("Total Order Value after Taxes and Discounts:", total_order_value)
