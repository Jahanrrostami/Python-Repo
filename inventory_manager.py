# Warm-up program 2
# Build a menu-based inventory manager for a store.
# This file is meant to prepare you for the larger student system.
# Each product dictionary should contain the following keys: 'id', 'name', 'price', 'quantity', and 'category'.
# Initialize the list with at least 10 sample products.
# Implement separate functions for each functionality.
# Try to handle errors where it makes sense.
# """
# Show a menu for the user with the following options:

# 1. Display all products
# 2. Add a new product
# 3. Update a product's information
# 4. Remove a product
# 5. Search for a product by name
# 6. Calculate total inventory value
# 7. Find the most expensive product
# 8. Find products with low stock (quantity < 5)
# 9. Generate a report of products by category
# 10. Update quantities (simulate a sale)
# 11. Exit the program
# """



# List
inventory = [
    {"id": 1 , "name": "Laptop", "price": 1000, "quantity": 5, "category": "Electronics"}
    ,{"id":2 , "name": "Mouse", "price": 30, "quantity": 30, "category": "Electronics"}
    ,{"id":3 , "name": "Keyboard", "price": 50, "quantity": 10, "category": "Electronics"}
    ,{"id":4 , "name": "Notebook", "price": 5, "quantity": 100, "category": "Stationary"}
    ,{"id":5 , "name": "Pen", "price": 0.6 , "quantity": 200 , "category": "Stationary"}
    ,{"id":6 , "name": "Desk Lamp", "price": 39, "quantity": 50, "category": "Stationary"}
    ,{"id":7 , "name": "Chair", "price": 30 , "quantity": 20, "category": "Furniture"}
    ,{"id":8 , "name": "Headphones", "price": 80, "quantity": 50 , "category": "Electronics"}
    ,{"id":9 , "name": "USB-Cable", "price": 10 , "quantity": 200, "category": "Electronics"}
    ,{"id":10 , "name": "Book", "price": 15, "quantity": 30, "category": "Stationary"}
]


def display_menue():
    print("1. Display all products")
    print("2. Add a new product")
    print("3. Update a product")
    print("4. Remove a product")
    print("5. Search by name")
    print("6. Total inventory value")
    print("7. Most expensive product")
    print("8. Low stock products")
    print("9. Report by category")
    print("10. Update quantities (sale)")
    print("11. Exit")


# Function to display all products
def display_all():
    if not inventory:
        print("No products.")
        return
    print("\nAll products:")
    for p in inventory:
        print(p['id'], p['name'], p['price'], p['quantity'], p['category'])


# Function to add products
def add_product():
    try:
        product_id = int(input("ID: "))
        name = input("Name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        category = input("Category: ")
        inventory.append({'id': product_id, 'name': name, 'price': price, 'quantity': quantity, 'category': category})
        print("Added.")
    except:
        print("Error.")   


# Function to update products 
def update_product():
    try:
        update_id = int(input("Enter the ID of the product you wish to update: "))
        for p in inventory:
            if p["id"] == update_id:
                print("Press Enter to keep old value")
                name = input("New name: ")
                if name: p["name"] = name
                price = input("New price: ")
                if price: p["price"] = float(price)
                quantity = input("New quantity: ")
                if quantity: p["quantity"] = int(quantity)
                category = input("New category: ")
                if category: p["category"] = category
                print("Product updated.")
                return
        print("Product not found.")
    except:
        print("Error.")


# Remove product function
def remove_product():
    try:
        remove_id = int(input("ID to remove: "))
        for i, p in enumerate(inventory):
            if p["id"] == remove_id:
                del inventory[i]
                print("Removed.")
                return
        print("Not found.")
    except:
        print("Error.")


# Search for product Function
def search_product():
    name = input("Name to search: ")
    for p in inventory:
        if p['name'] == name:
            print(p['id'], p['name'], p['price'], p['quantity'])
            return
    print("Not found.")

# Calculate total value function
def calculate_total_value():
    total = 0
    for p in inventory:
        total += p['price'] * p['quantity']
    print("Total value:", total)

# Find Pricy function
def find_most_expensive():
    if not inventory:
        print("No products.")
        return
    max_p = max(inventory, key=lambda p: p['price'])
    print("Most expensive:", max_p['name'], max_p['price'])

# Find least amount of stock function
def find_low_stock():
    print("\nLow stock:")
    found = False
    for p in inventory:
        if p['quantity'] < 5:
            print(p['id'], p['name'], p['quantity'])
            found = True
    if not found:
        print("None.")

# Report function
def generate_category_report():
    print("\nReport by category:")
    report = {}
    for p in inventory:
        cat = p['category']
        if cat not in report:
            report[cat] = []
        report[cat].append(p)
    for cat in report:
        print(cat, ":")
        for p in report[cat]:
            print("  -", p['name'], "(Qty:", p['quantity'], ")")

# Update qunatity
def update_quantities():
    try:
        product_id = int(input("ID to sell: "))
        qty = int(input("Quantity sold: "))
        for p in inventory:
            if p['id'] == product_id:
                if p['quantity'] >= qty:
                    p['quantity'] -= qty
                    print("Sale done. New qty:", p['quantity'])
                else:
                    print("Not enough stock.")
                return
        print("Not found.")
    except:
        print("Error.")
                   
# Display code
while True:
    display_menue()
    choice = input("\nChoice (1-11): ")

    if choice == "1":
        display_all()
    elif choice == "2":
        add_product()
    elif choice == "3":
        update_product()
    elif choice == "4":
        remove_product()
    elif choice == "5":
        search_product()
    elif choice == "6":
        calculate_total_value()
    elif choice == "7":
        find_most_expensive()
    elif choice == "8":
        find_low_stock()
    elif choice == "9":
        generate_category_report()
    elif choice == "10":
        update_quantities()
    elif choice == "11":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")