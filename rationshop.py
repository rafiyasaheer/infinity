class RationShop:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity, price):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'quantity': quantity, 'price': price}
        print(f"Added {quantity} of {item_name} at {price} each.")

    def display_items(self):
        if not self.items:
            print("No items available in the shop.")
            return
        print("Available items in the shop:")
        for item_name, details in self.items.items():
            print(f"{item_name}: Quantity = {details['quantity']}, Price = {details['price']}")

    def sell_item(self, item_name, quantity):
        if item_name in self.items:
            if self.items[item_name]['quantity'] >= quantity:
                self.items[item_name]['quantity'] -= quantity
                total_price = quantity * self.items[item_name]['price']
                print(f"Sold {quantity} of {item_name}. Total price: {total_price}")
            else:
                print(f"Insufficient stock for {item_name}. Available quantity: {self.items[item_name]['quantity']}")
        else:
            print(f"{item_name} is not available in the shop.")

    def check_stock(self, item_name):
        if item_name in self.items:
            print(f"{item_name}: Available quantity = {self.items[item_name]['quantity']}")
        else:
            print(f"{item_name} is not available in the shop.")


def main():
    shop = RationShop()

    while True:
        print("\nRation Shop Management System")
        print("1. Add Item")
        print("2. Display Items")
        print("3. Sell Item")
        print("4. Check Stock")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            shop.add_item(item_name, quantity, price)

        elif choice == '2':
            shop.display_items()

        elif choice == '3':
            item_name = input("Enter item name to sell: ")
            quantity = int(input("Enter quantity to sell: "))
            shop.sell_item(item_name, quantity)

        elif choice == '4':
            item_name = input("Enter item name to check stock: ")
            shop.check_stock(item_name)

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()