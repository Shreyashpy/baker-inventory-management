import datetime

# Global inventory list
inventory = []

# Load inventory from file
def load_inventory():
    global inventory
    inventory = []
    try:
        with open('inventory.txt', 'r') as f:
            for line in f.readlines():
                name, quantity, price, expiry_date,
                quantity_used = line.strip().split(',')
                item = {
                    "name": name,
                    "quantity": int(quantity),
                    "price": float(price),
                    "expiry_date": expiry_date,
                    "quantity_used": int(quantity_used)
                }
                inventory.append(item)
    except FileNotFoundError:
        inventory = []
    except Exception as e:
        print(f"Error loading inventory: {e}")

# Save inventory to file
def save_inventory():
    try:
        with open('inventory.txt', 'w') as f:
            for item in inventory:
                line = f"{item['name']},{item['quantity']},
                {item['price']},{item['expiry_date']},
                {item['quantity_used']}\n"
                f.write(line)
        print("Inventory successfully saved to 'inventory.txt'.")
    except Exception as e:
        print(f"Error saving inventory: {e}")

# Add multiple items to the inventory
def add_item():
    while True:
        name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: "))
        expiry_date = input("Enter expiry date (YYYY-MM-DD): ")

        item = {
            "name": name,
            "quantity": quantity,
            "price": price,
            "expiry_date": expiry_date,
            "quantity_used": 0
        }
        inventory.append(item)
        save_inventory()
        print(f"Item '{name}' added successfully!\n")

        choice = input("Do you want to add more item? (y/n): ").lower()
        if choice != 'y':
            break

# View current inventory
def view_inventory():
    print("\nCurrent Inventory:")
    for item in inventory:
        print(f"Name: {item['name']},
              Quantity: {item['quantity']}, Price: {item['price']},
              Expiry Date: {item['expiry_date']}")
    print()

# Update item quantity after sale
def update_item_quantity():
    name = input("Enter item name to update after sale: ")
    sold_quantity = int(input("Enter quantity sold: "))

    for item in inventory:
        if item['name'].lower() == name.lower():
            if item['quantity'] >= sold_quantity:
                item['quantity'] -= sold_quantity
                item['quantity_used'] += sold_quantity
                save_inventory()
                print(f"{sold_quantity} units of '{name}' sold and updated in inventory.")
            else:
                print(f"Not enough stock of '{name}'. Current stock: {item['quantity']}")
            return
    print(f"Item '{name}' not found in inventory.")

# Generate a sales report
def generate_sales_report():
    report_content = "Sales Report\n\n"
    report_content += "Item Name\tQuantity Sold\tTotal Revenue\tQuantity Left\n"

    for item in inventory:
        revenue = item['quantity_used'] * item['price']
        report_content += f"{item['name']}\t{item['quantity_used']}\t₹{revenue:.2f}\t{item['quantity']}\n"

    with open("sales_report.txt", "w", encoding="utf-8") as report_file:
        report_file.write(report_content)

    print("Sales report generated and saved as 'sales_report.txt'.")

# Search for an item by name or expiry date
def search_item():
    search_term = input("Enter item name or expiry date (YYYY-MM-DD) to search: ").lower()
    print("\nSearch Results:")
    found = False
    for item in inventory:
        if search_term in item['name'].lower() or search_term == item['expiry_date']:
            print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}, Expiry Date: {item['expiry_date']}")
            found = True
    if not found:
        print("No matching items found.")

# Display low stock items
def low_stock_alert():
    print("\nLow Stock Items (Quantity < 10):")
    found = False
    for item in inventory:
        if item['quantity'] < 10:
            print(f"Name: {item['name']}, Quantity: {item['quantity']}")
            found = True
    if not found:
        print("No low stock items.")

# Display expiry alerts
def expiry_alert():
    today = datetime.date.today()
    print("\nItems Close to Expiry (Within 7 Days):")
    found = False
    for item in inventory:
        expiry_date = datetime.datetime.strptime(item['expiry_date'], '%Y-%m-%d').date()
        days_left = (expiry_date - today).days
        if days_left <= 7:
            print(f"Name: {item['name']}, Expiry Date: {item['expiry_date']}, Days Left: {days_left}")
            found = True
    if not found:
        print("No items close to expiry.")

# Sort inventory alphabetically
def sort_inventory():
    global inventory
    inventory = sorted(inventory, key=lambda x: x['name'].lower())
    print("\nInventory sorted alphabetically.")
    view_inventory()

# Check for items expiring before a specific date
def items_expiring_before_date():
    date_input = input("Enter a date (YYYY-MM-DD) to find items expiring before that date: ")
    try:
        input_date = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
        print(f"\nItems Expiring Before {date_input}:")
        found = False
        for item in inventory:
            expiry_date = datetime.datetime.strptime(item['expiry_date'], '%Y-%m-%d').date()
            if expiry_date < input_date:
                print(f"Name: {item['name']}, Expiry Date: {item['expiry_date']}, Quantity: {item['quantity']}")
                found = True
        if not found:
            print("No items are expiring before the specified date.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD format.")

# Main menu
def main():
    load_inventory()
    while True:
        print("\n--- Bakery Inventory Management ---")
        print("1. Add New Item(s)")
        print("2. View Inventory")
        print("3. Update Item Quantity After Sale")
        print("4. Generate Sales Report")
        print("5. Search Item by Name")
        print("6. Low Stock Alert")
        print("7. Expiry Alert")
        print("8. Sort Inventory Alphabetically")
        print("9. Items Expiring Before a Specific Date")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_item()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            update_item_quantity()
        elif choice == '4':
            generate_sales_report()
        elif choice == '5':
            search_item()
        elif choice == '6':
            low_stock_alert()
        elif choice == '7':
            expiry_alert()
        elif choice == '8':
            sort_inventory()
        elif choice == '9':
            items_expiring_before_date()
        elif choice == '10':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
