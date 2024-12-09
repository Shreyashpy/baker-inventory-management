# File path for the inventory data
inventory_file = 'inventory.txt'

# Try opening the file; if it doesn't exist, create it
try:
    with open(inventory_file, 'r') as f:
        pass  # File exists, do nothing
except FileNotFoundError:
    # Create the file if it doesn't exist
    with open(inventory_file, 'w') as f:
        pass  # Create an empty file

# Main menu
while True:
    print("\n==== Inventory Management System ====")
    print("1. Add Item")
    print("2. Update Item Quantity")
    print("3. Use Item")
    print("4. View Inventory")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':  # Add Item
        name = input("Enter the item name: ")
        quantity = int(input(f"Enter quantity of {name}: "))

        # Loading inventory from file
        inventory = {}
        with open(inventory_file, 'r') as f:
            for line in f:
                if line.strip():  # Check if line is not empty
                    item, qty = line.strip().split(',')
                    inventory[item] = int(qty)
        
        # Adding new item or checking if it exists
        if name in inventory:
            print(f"Item '{name}' already exists in the inventory with quantity {inventory[name]}. Use update option to change quantity.")
        else:
            inventory[name] = quantity
            with open(inventory_file, 'w') as f:
                for item, qty in inventory.items():
                    f.write(f"{item},{qty}\n")
            print(f"Item '{name}' added with quantity {quantity}.")

    elif choice == '2':  # Update Item Quantity
        name = input("Enter the item name: ")
        quantity = int(input(f"Enter quantity to add/subtract for {name} (use negative numbers to subtract): "))

        # Loading inventory from file
        inventory = {}
        with open(inventory_file, 'r') as f:
            for line in f:
                if line.strip():  # Check if line is not empty
                    item, qty = line.strip().split(',')
                    inventory[item] = int(qty)

        # Updating item quantity
        if name in inventory:
            inventory[name] += quantity
            if inventory[name] < 0:
                inventory[name] = 0  # Preventing negative quantities
            with open(inventory_file, 'w') as f:
                for item, qty in inventory.items():
                    f.write(f"{item},{qty}\n")
            print(f"Item '{name}' quantity updated to {inventory[name]}.")
        else:
            print(f"Item '{name}' does not exist in the inventory.")

    elif choice == '3':  # Use Item
        name = input("Enter the item name: ")
        quantity = int(input(f"Enter quantity to use for {name}: "))

        # Loading inventory from file
        inventory = {}
        with open(inventory_file, 'r') as f:
            for line in f:
                if line.strip():  # Check if line is not empty
                    item, qty = line.strip().split(',')
                    inventory[item] = int(qty)

        # Using the item and reducing quantity
        if name in inventory:
            if inventory[name] >= quantity:
                inventory[name] -= quantity
                print(f"Item '{name}' quantity decreased by {quantity}.")
            else:
                print(f"Not enough quantity of '{name}'. Reducing to 0.")
                inventory[name] = 0
            with open(inventory_file, 'w') as f:
                for item, qty in inventory.items():
                    f.write(f"{item},{qty}\n")
            print(f"New quantity of '{name}': {inventory[name]}")
        else:
            print(f"Item '{name}' does not exist in inventory.")

    elif choice == '4':  # View Inventory
        # Loading inventory from file
        inventory = {}
        with open(inventory_file, 'r') as f:
            for line in f:
                if line.strip():  # Check if line is not empty
                    item, qty = line.strip().split(',')
                    inventory[item] = int(qty)

        # Displaying inventory
        print("\nCurrent Inventory:")
        if inventory:
            for item, qty in inventory.items():
                print(f"Item: {item}, Quantity: {qty}")
        else:
            print("Inventory is empty.")

    elif choice == '5':  # Exit the program
        print("Exiting the program.")
        break

    else:
        print("Invalid choice! Please choose a valid option.")

# ======= Inventory Management System Operations =======
# 1. Add Item: Add a new item with its quantity to the inventory.
# 2. Update Item Quantity: Increase or decrease the quantity of an existing item.
# 3. Use Item: Use a certain quantity of an item, reducing its quantity.
# 4. View Inventory: View the current inventory of items and their quantities.
# 5. Exit: Exit the inventory management system.

