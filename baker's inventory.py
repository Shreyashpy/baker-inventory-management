import csv

# File path for the CSV inventory data
inventory_file = 'inventory.csv'

# Function to load existing inventory data from CSV file
def load_inventory():
    try:
        with open(inventory_file, mode='r', newline='') as f:
            reader = csv.DictReader(f)
            inventory = {row['Item']: int(row['Quantity']) for row in reader}
    except FileNotFoundError:
        inventory = {}
    return inventory

# Function to save current inventory data to CSV file
def save_inventory(inventory):
    with open(inventory_file, mode='w', newline='') as f:
        fieldnames = ['Item', 'Quantity']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item, quantity in inventory.items():
            writer.writerow({'Item': item, 'Quantity': quantity})

# Function to add a new item to the inventory
def add_item(name, quantity):
    inventory = load_inventory()
    if name in inventory:
        print(f"Item '{name}' already exists in inventory.")
    else:
        inventory[name] = quantity
        save_inventory(inventory)
        print(f"Item '{name}' added with quantity {quantity}.")

# Function to update the quantity of an existing item in the inventory
def update_item(name, quantity):
    inventory = load_inventory()
    if name in inventory:
        inventory[name] += quantity
        if inventory[name] < 0:
            inventory[name] = 0  # Prevent negative quantities
        save_inventory(inventory)
        print(f"Item '{name}' quantity updated to {inventory[name]}.")
    else:
        print(f"Item '{name}' does not exist in inventory.")

# Function to use a specified quantity of an item in the inventory
def use_item(name, quantity):
    inventory = load_inventory()
    if name in inventory:
        if inventory[name] >= quantity:
            inventory[name] -= quantity
        else:
            print(f"Not enough quantity of '{name}' to use {quantity}.")
            inventory[name] = 0  # Set quantity to zero if it goes negative
        save_inventory(inventory)
        print(f"Item '{name}' quantity decreased by {quantity}. New quantity: {inventory[name]}.")
    else:
        print(f"Item '{name}' does not exist in inventory.")

# Function to view all items in the inventory
def view_inventory():
    inventory = load_inventory()
    print("Current Inventory:")
    for item, quantity in inventory.items():
        print(f"Item: {item}, Quantity: {quantity}")

# Function to generate a simple inventory report
def generate_report():
    inventory = load_inventory()
    with open('inventory_report.txt', 'w') as f:
        f.write("Inventory Report\n")
        f.write("================\n")
        for item, quantity in inventory.items():
            f.write(f"Item: {item}, Quantity: {quantity}\n")
    print("Report generated: inventory_report.txt")

# Example Usage
#add_item('Bread', 50)
#update_item('Bread', 10)
#use_item('Bread', 5)  # New function usage example
#add_item('Milk', 20)
#view_inventory()
#generate_report()
