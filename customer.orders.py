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
            {"productName": "Blender", "price": 49.99, "quantity": 1}
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

# Example: print all customer names and their orders
for customer in customers:
    print(f"Customer: {customer['name']}")
    for order in customer['orders']:
        print(f"  Product: {order['productName']}, Price: {order['price']}, Quantity: {order['quantity']}")

print("===================================")
#Print hign spender customer
highest_spender = None
highest_amount = 0  
for customer in customers:
    total_spent = sum(order['price'] * order['quantity'] for order in customer['orders'])
    if total_spent > highest_amount:
        highest_amount = total_spent
        highest_spender = customer['name']
print(f"Highest spender: {highest_spender} with amount: ${highest_amount:.2f}")
print("===================================")

# Example: Calculate how many customers ordered a specific product
product_to_check = "Blender"
customers_who_ordered = {"name":" ","orders":[]}; 
count = 0
for customer in customers:
    for order in customer['orders']:
        if order['productName'] == product_to_check:
            if customer['name'] not in customers_who_ordered:
                customers_who_ordered['name'] = customer['name']
                customers_who_ordered['orders'].append(order)
                count += sum(1 for o in order['quantity'])
                print(count)
            #print(customers_who_ordered['name'] + " ordered : {product_to_check}  + "Number of times ordered ": {count})
            print(f"{customer['name']} ordered {product_to_check}")

times_ordered = sum(1 for customer in customers if any(order['productName'] == product_to_check for order in customer['orders']))
print(f"Number of customers who ordered {product_to_check}: {times_ordered}")

customers_who_ordered = [customer['name'] for customer in customers if any(order['productName']
== product_to_check for order in customer['orders'])]
print("===================================")