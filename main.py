import getpass

# Define Product class
class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"{self.product_id} - {self.name} | {self.category} | ${self.price} | Stock: {self.stock_quantity}"

# Inventory Management System
class InventoryManagementSystem:
    def __init__(self):
        self.products = {}
        self.low_stock_threshold = 5

    def add_product(self, product):
        self.products[product.product_id] = product
        print(f"Product {product.name} added successfully.")

    def update_product(self, product_id, name=None, category=None, price=None, stock_quantity=None):
        product = self.products.get(product_id)
        if not product:
            print("Product not found.")
            return
        if name:
            product.name = name
        if category:
            product.category = category
        if price is not None:
            product.price = price
        if stock_quantity is not None:
            product.stock_quantity = stock_quantity
        print(f"Product {product.product_id} updated successfully.")

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print(f"Product {product_id} deleted successfully.")
        else:
            print("Product not found.")

    def view_inventory(self):
        for product in self.products.values():
            print(product)
            if product.stock_quantity <= self.low_stock_threshold:
                print(f"  **Low Stock Alert: {product.name}**")

    def search_product(self, name):
        found_products = [p for p in self.products.values() if name.lower() in p.name.lower()]
        for product in found_products:
            print(product)
        if not found_products:
            print("No products found.")

    def filter_by_category(self, category):
        filtered_products = [p for p in self.products.values() if p.category.lower() == category.lower()]
        for product in filtered_products:
            print(product)
        if not filtered_products:
            print("No products found in this category.")

    def adjust_stock(self, product_id, quantity):
        product = self.products.get(product_id)
        if not product:
            print("Product not found.")
            return
        product.stock_quantity += quantity
        print(f"Stock updated for {product.name}. New stock quantity: {product.stock_quantity}")

# User management for role-based access
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

# Simple role-based authentication system
class AuthenticationSystem:
    def __init__(self):
        self.users = {
            "admin": User("admin", "Admin"),
            "user": User("user", "User")
        }
        self.credentials = {
            "admin": "admin123",
            "user": "user123"
        }

    def authenticate(self):
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        if username in self.credentials and self.credentials[username] == password:
            print(f"Welcome, {username}!")
            return self.users[username]
        else:
            print("Authentication failed.") 

# Main system controller
def main():
    auth_system = AuthenticationSystem()
    ims = InventoryManagementSystem()

    user = auth_system.authenticate()
    if not user:
        return

    while True:
        try:
            print("\n--- Bakery Inventory Management System ---")
            if user.role == "Admin":
                print("1. Add Product")
                print("2. Update Product")
                print("3. Delete Product")
                print("4. View Inventory")
                print("5. Search Product")
                print("6. Filter by Category")
                print("7. Adjust Stock")
                print("0. Exit")

                choice = int(input("Choose an option: "))
                if choice == 1:
                    product_id = input("Enter Product ID: ")
                    name = input("Enter Product Name: ")
                    category = input("Enter Category: ")
                    price = float(input("Enter Price: "))
                    stock_quantity = int(input("Enter Stock Quantity: "))
                    product = Product(product_id, name, category, price, stock_quantity)
                    ims.add_product(product)

                elif choice == 2:
                    product_id = input("Enter Product ID to update: ")
                    name = input("Enter new name (leave blank to skip): ")
                    category = input("Enter new category (leave blank to skip): ")
                    price = input("Enter new price (leave blank to skip): ")
                    stock_quantity = input("Enter new stock quantity (leave blank to skip): ")
                    ims.update_product(
                        product_id,
                        name=name if name else None,
                        category=category if category else None,
                        price=float(price) if price else None,
                        stock_quantity=int(stock_quantity) if stock_quantity else None
                    )

                elif choice == 3:
                    product_id = input("Enter Product ID to delete: ")
                    ims.delete_product(product_id)

                elif choice == 4:
                    ims.view_inventory()

                elif choice == 5:
                    name = input("Enter product name to search: ")
                    ims.search_product(name)

                elif choice == 6:
                    category = input("Enter category to filter by: ")
                    ims.filter_by_category(category)

                elif choice == 7:
                    product_id = input("Enter Product ID to adjust stock: ")
                    quantity = int(input("Enter quantity to add/subtract: "))
                    ims.adjust_stock(product_id, quantity)

                elif choice == 0:
                    break
                else:
                    print("Invalid option. Please try again.")

            elif user.role == "User":
                print("1. View Inventory")
                print("2. Search Product")
                print("3. Filter by Category")
                print("0. Exit")

                choice = int(input("Choose an option: "))
                if choice == 1:
                    ims.view_inventory()
                elif choice == 2:
                    name = input("Enter product name to search: ")
                    ims.search_product(name)
                elif choice == 3:
                    category = input("Enter category to filter by: ")
                    ims.filter_by_category(category)
                elif choice == 0:
                    break
                else:
                    print("Invalid option. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a valid option.")


if __name__ == "__main__":
    main()
