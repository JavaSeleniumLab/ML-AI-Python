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
            {"productName": "Blender", "price": 49.99, "quantity": 5}
        ]
    },
     {
        "name": "Alina Kuch",
        "id": 77777,
        "orders": [
            {"productName": "Laptop", "price": 599.99, "quantity": 1},
            {"productName": "Smart-Watch", "price": 199.99, "quantity": 1},
            {"productName": "Air-Fryer", "price": 150.10, "quantity": 1},
            {"productName": "Blender", "price": 49.99, "quantity": 2}
        ]
    }, 
     {
        "name": "Ellie Johnson",
        "id": 88888,
        "orders": [
            {"productName": "Air-Fryer", "price": 200.50, "quantity": 5},
            {"productName": "Blender", "price": 49.99, "quantity": 1},
            {"productName": "Blender", "price": 49.99, "quantity": 1},
            {"productName": "Blender", "price": 49.99, "quantity": 8}
        ]
    }

]

# Track unique products and customers using sets
unique_products = set()
unique_customers = set()

for customer in customers:
    unique_customers.add(customer['name'])
    for order in customer['orders']:
        unique_products.add(order['productName'])

print(f"Unique customers: {unique_customers}")
print(f"Unique products: {unique_products}")

print("===================================")

# Print all customer names and their orders
for customer in customers:
    print(f"Customer: {customer['name']}")
    for order in customer['orders']:
        print(f"  Product: {order['productName']}, Price: {order['price']}, Quantity: {order['quantity']}")

print("===================================")
# Print hign spender customer
highest_spender = None
highest_amount = 0  
for customer in customers:
    total_spent = sum(order['price'] * order['quantity'] for order in customer['orders'])
    if total_spent > highest_amount:
        highest_amount = total_spent
        highest_spender = customer['name']
print(f"Highest spender: {highest_spender} with amount: ${highest_amount:.2f}")

print("===================================")

# Summing up total spending per customer
#name_to_check = "Alina Kuch"
for customer in customers:
        total_spent = sum(order['price'] * order['quantity'] for order in customer['orders'])
        print(f"{customer['name']} spent total: ${total_spent:.2f}")

print("===================================")

# Example: Calculate how many times customers ordered a specific product
product_to_check = "Blender"

for customer in customers:
        count = 0
        for order in customer['orders']:
                 if order['productName'] == product_to_check : 
                  count += order['quantity']
        print(f"{customer['name']} ordered {product_to_check} - {count} times")
            
print("===================================")

# Sum up total sales per product.
product_sales = {}
for customer in customers:
    for order in customer['orders']:
        product = order['productName']
        total = order['price'] * order['quantity']
        if product in product_sales:
            product_sales[product] += total
        else:
            product_sales[product] = total

for product, total in product_sales.items():
    print(f"Total sales for {product}: ${total:.2f}")

   