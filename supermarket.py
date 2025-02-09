import os
import time

products = []


def clear_console_and_redirect():
    time.sleep(3)
    os.system("cls")


def clear_console_and_wait():
    input("\nPress any key to continue...")
    os.system("cls")


def validate_input_str(descriptor):
    while True:
        user_input = input(f"Enter {descriptor}: ")
        if user_input.isalpha():
            return user_input
        else:
            print("Invalid input. Please try again.\n")


def validate_input_int(descriptor):
    while True:
        user_input = input(f"Enter {descriptor}: ")
        if user_input.isdigit():
            return user_input
        else:
            print("Invalid input. Please try again.\n")


def validate_input_float(descriptor):
    while True:
        user_input = input(f"Enter {descriptor}: ")
        if user_input.replace(".", "", 1).isdigit():
            return user_input
        else:
            print("Invalid input. Please try again.\n")


def add_product(name, price, quantity):
    products.append(
        {"name": name.lower(), "price": price, "quantity": quantity}
    )

    print("Product added successfully! Returning to menu...")
    clear_console_and_redirect()


def delete_product(name):
    name = name.lower()
    for i, product in enumerate(products):
        if product["name"] == name:
            products.pop(i)
            print("Product deleted successfully! Returning to menu...")
            clear_console_and_redirect()

    print("Product deleted successfully! Returning to menu...")
    clear_console_and_redirect()
    return


def modify_product(name, new_name, new_price, new_quantity):
    name = name.lower()
    for product in products:
        if product["name"] == name:
            product["name"] = new_name.lower()
            product["price"] = float(new_price)
            product["quantity"] = int(new_quantity)

    print("Product modified successfully! Returning to menu...")
    clear_console_and_redirect()
    return


def count_products():
    return len(products)


def print_products_names():
    for product in products:
        print(product["name"].capitalize())


def print_products():
    for product in products:
        for key, value in product.items():
            print(
                f"{key.capitalize()}: {value.capitalize() if key == 'name' else value}"
            )
        print("\n")

    clear_console_and_wait()


while True:
    print("----------------------")
    print("|     Supermarket    |")
    print("----------------------")
    print("\n")
    print(f"All products: {count_products()}")
    print("\n")
    print("----------------------")
    print("|    Menu Options    |")
    print("----------------------")
    print("\n")
    print("1. Add product")
    print("2. Delete product")
    print("3. Modify product")
    print("4. Show all products")
    print("5. Exit")
    print("\n")

    choice = input(">_ ")
    print("\n\n")

    if choice == "1":
        print("Add product:\n")
        name = validate_input_str("name")

        if name.lower() in [product["name"] for product in products]:
            print("Product already exists. Returning to menu...")
            clear_console_and_redirect()
            continue

        price = validate_input_float("price")
        quantity = validate_input_int("quantity")

        add_product(name, price, quantity)

    elif choice == "2":
        print("Delete product:\n")

        if count_products() == 0:
            print("No products to delete. Returning to menu...")
            clear_console_and_redirect()
            continue

        print_products_names()

        name = validate_input_str("name")

        if name.lower() not in [product["name"] for product in products]:
            print("Product not found. Returning to menu...")
            clear_console_and_redirect()
            continue

        delete_product(name)

    elif choice == "3":
        print("Modify product:\n")

        if count_products() == 0:
            print("No products to delete. Returning to menu...")
            clear_console_and_redirect()
            continue

        print_products_names()

        name = validate_input_str("name")

        if name.lower() not in [product["name"] for product in products]:
            print("Product not found. Returning to menu...")
            clear_console_and_redirect()
            continue

        new_name = validate_input_str("new name")
        new_price = validate_input_float("new price")
        new_quantity = validate_input_int("new quantity")

        modify_product(name, new_name, new_price, new_quantity)

    elif choice == "4":
        print("All products:\n")
        print_products()

    elif choice == "5":
        break

    else:
        print("Invalid choice. Please try again.\n")
        clear_console_and_redirect()
