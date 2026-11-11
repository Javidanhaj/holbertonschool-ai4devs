# Goal: Add up order prices, skipping orders without a price.

def calculate_total(orders):
    total = 0
    for order in orders:
        if "price" in order:
            total += order["price"]
    return total


orders = [
    {"item": "Notebook", "price": 12},
    {"item": "Pen", "price": 3},
    {"item": "Free sample"},
    {"item": "Folder", "price": 5},
]

print("Order total:", calculate_total(orders))
print("Expected total: 20")
