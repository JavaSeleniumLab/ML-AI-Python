customers = [
    {
        "name": "John Doe",
        "id": 12345,
        "orders": [
            {"productName": "Laptop", "price": 999.99, "quantity": 1}
        ]
    },
    {
        "name": "Jane Smith",
        "id": 67890,
        "orders": [
            {"productName": "T-shirt", "price": 19.99, "quantity": 2},
            {"productName": "Blender", "price": 49.99, "quantity": 1}
        ]
    }
]

# Example: print all customer names and their orders
for customer in customers:
    print(f"Customer: {customer['name']}")
    for order in customer['orders']:
        print(f"  Product: {order['productName']}, Price: {order['price']}, Quantity: {order['quantity']}")