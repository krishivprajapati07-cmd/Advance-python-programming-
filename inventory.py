class Product:
    def __init__(self, product_id, product_name, price, category):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.category = category

    def display(self):
        print("Product ID   :", self.product_id)
        print("Product Name :", self.product_name)
        print("Price        :", self.price)
        print("Category     :", self.category)
        print("-" * 35)


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print("Product added successfully!")

    def display_all(self):
        if len(self.products) == 0:
            print("No product records found.")
        else:
            print("\n===== Product Inventory =====")
            for product in self.products:
                product.display()


# Main Program
inventory = Inventory()

while True:
    print("\n===== Product Inventory System =====")
    print("1. Add Product")
    print("2. Display All Products")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        product_id = input("Enter Product ID: ")
        product_name = input("Enter Product Name: ")
        price = float(input("Enter Product Price: "))

        print("Select Product Category:")
        print("1. Expensive")
        print("2. Affordable")

        category_choice = input("Enter category: ")

        if category_choice == "1":
            category = "Expensive"
        elif category_choice == "2":
            category = "Affordable"
        else:
            print("Invalid category!")
            continue

        product = Product(product_id, product_name, price, category)
        inventory.add_product(product)

    elif choice == "2":
        inventory.display_all()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")