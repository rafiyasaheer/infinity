import sqlite3

# Connect to SQLite Database
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# Create Tables
cursor.execute('''CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE,
                    price REAL,
                    stock INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS sales (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    item_name TEXT,
                    quantity INTEGER,
                    total_price REAL,
                    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

conn.commit()

def add_item():
    name = input("Enter item name: ").strip()
    price = float(input("Enter item price: "))
    stock = int(input("Enter stock quantity: "))
    
    try:
        cursor.execute("INSERT INTO items (name, price, stock) VALUES (?, ?, ?)", (name, price, stock))
        conn.commit()
        print("Item added successfully!")
    except sqlite3.IntegrityError:
        print("Item already exists.")

def update_stock():
    name = input("Enter item name to update stock: ").strip()
    new_stock = int(input("Enter new stock quantity: "))
    
    cursor.execute("UPDATE items SET stock = ? WHERE name = ?", (new_stock, name))
    if cursor.rowcount > 0:
        conn.commit()
        print("Stock updated successfully!")
    else:
        print("Item not found.")

def view_items():
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    
    if items:
        print("\nAvailable Items:")
        print("ID | Name | Price | Stock")
        for item in items:
            print(f"{item[0]} | {item[1]} | ₹{item[2]:.2f} | {item[3]}")
    else:
        print("No items available.")

def sell_item():
    view_items()
    item_name = input("Enter item name to purchase: ").strip()
    quantity = int(input("Enter quantity: "))
    
    cursor.execute("SELECT price, stock FROM items WHERE name = ?", (item_name,))
    item = cursor.fetchone()
    
    if item and item[1] >= quantity:
        total_price = item[0] * quantity
        new_stock = item[1] - quantity

        cursor.execute("UPDATE items SET stock = ? WHERE name = ?", (new_stock, item_name))
        cursor.execute("INSERT INTO sales (item_name, quantity, total_price) VALUES (?, ?, ?)",
                       (item_name, quantity, total_price))
        conn.commit()
        print(f"Purchase successful! Total cost: ₹{total_price:.2f}")
    else:
        print("Insufficient stock or item not found.")

def view_sales():
    cursor.execute("SELECT * FROM sales")
    sales = cursor.fetchall()
    
    if sales:
        print("\nSales Report:")
        print("ID | Item Name | Quantity | Total Price | Date")
        for sale in sales:
            print(f"{sale[0]} | {sale[1]} | {sale[2]} | ₹{sale[3]:.2f} | {sale[4]}")
    else:
        print("No sales recorded yet.")

def main():
    while True:
        print("\n=== Ration Shop Management ===")
        print("1. Add New Item")
        print("2. Update Stock")
        print("3. View Items")
        print("4. Sell Item")
        print("5. View Sales Report")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_item()
        elif choice == "2":
            update_stock()
        elif choice == "3":
            view_items()
        elif choice == "4":
            sell_item()
        elif choice == "5":
            view_sales()
        elif choice == "6":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    try:
        main()
    finally:
        conn.close()  # Ensure the database connection is closed on exit