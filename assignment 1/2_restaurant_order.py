# Question 2: Restaurant Orders and Daily Collection

menu = {
    1: ("Momo", 180),
    2: ("Chowmein", 150),
    3: ("Thakali Set", 450),
    4: ("Lassi", 120)
}

orders = [
    "1:2,4:2",
    "3:1,1:1,9:3",
    "2:3,1:2,4:1"
]

# Initialize variables
items_sold = {}
invalid_codes = []
daily_collection = 0

# Process each table's order
for i, order in enumerate(orders, start=1):

    subtotal = 0

    # Split order into individual items
    order_items = order.split(",")

    for item in order_items:

        code, quantity = item.split(":")

        code = int(code)
        quantity = int(quantity)

        # Skip unknown menu codes
        if code not in menu:
            if code not in invalid_codes:
                invalid_codes.append(code)
            continue

        name, price = menu[code]

        subtotal += price * quantity

        # Count quantity sold
        if name not in items_sold:
            items_sold[name] = 0

        items_sold[name] += quantity

    # Calculate service charge and VAT
    service_charge = subtotal * 0.10

    vat = (subtotal + service_charge) * 0.13

    final_bill = subtotal + service_charge + vat

    daily_collection += final_bill

    print(
        f"Table {i}: subtotal Rs {subtotal}, "
        f"bill with service + VAT Rs {final_bill:.2f}"
    )

# Find best seller
best_seller = max(items_sold, key=items_sold.get)

print("Items sold:", items_sold)

print(
    f"Best seller: {best_seller} | "
    f"Invalid codes: {invalid_codes}"
)

print(f"Day's collection: Rs {daily_collection:.2f}")