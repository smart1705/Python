def display_menu(menu):
    print("\n----- FOOD MENU -----")
    print("ID\tFood Name\tPrice")

    for item_id, item in menu.items():
        print(item_id, "\t", item["name"], "\t\t₹", item["price"])


def search_food(menu):
    while True:
        name = input("Enter food name to search: ").strip()

        if name:
            break

        print("Error: Food name cannot be empty.")

    found = False

    for item_id, item in menu.items():
        if name.casefold() in item["name"].casefold():
            print(item_id, "-", item["name"], "- ₹", item["price"])
            found = True

    if not found:
        print("Food item not found.")


def enter_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity > 0:
                return quantity
            else:
                print("Error: Quantity must be greater than zero.")

        except ValueError:
            print("Error: Enter a valid whole number.")


def enter_item_id(menu, message):
    while True:
        item_id = input(message).strip().upper()

        if item_id in menu:
            return item_id
        else:
            print("Error: Invalid food item ID.")


def add_to_cart(menu, cart):
    item_id = enter_item_id(menu, "Enter food item ID: ")
    quantity = enter_quantity()

    if item_id in cart:
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    print("Item added to cart successfully.")


def remove_from_cart(menu, cart):
    if not cart:
        print("Your cart is empty.")
        return

    while True:
        item_id = input("Enter item ID to remove: ").strip().upper()

        if item_id in cart:
            del cart[item_id]
            print("Item removed from cart.")
            return
        elif item_id not in menu:
            print("Error: Invalid food item ID.")
        else:
            print("Item not found in cart.")


def view_cart(menu, cart):
    if not cart:
        print("Your cart is empty.")
        return

    print("\n----- YOUR CART -----")
    print("Food\t\tPrice\tQuantity\tCost")

    for item_id, quantity in cart.items():
        item = menu[item_id]
        cost = item["price"] * quantity

        print(item["name"], "\t\t", item["price"],
              "\t", quantity, "\t\t₹", cost)


def calculate_bill(menu, cart):
    total = 0

    for item_id, quantity in cart.items():
        total += menu[item_id]["price"] * quantity

    if total >= 500:
        discount = total * 0.10
    else:
        discount = 0

    final_amount = total - discount

    return total, discount, final_amount


def display_bill(menu, cart):
    if not cart:
        print("Your cart is empty.")
        return

    view_cart(menu, cart)
    total, discount, final_amount = calculate_bill(menu, cart)

    print("\nOriginal Bill: ₹", round(total, 2))
    print("Discount: ₹", round(discount, 2))
    print("Final Bill: ₹", round(final_amount, 2))


def place_order(menu, cart):
    if not cart:
        print("Cannot place order. Your cart is empty.")
        return

    display_bill(menu, cart)

    while True:
        confirm = input("Confirm order? (yes/no): ").strip().casefold()

        if confirm == "yes":
            print("\nOrder placed successfully!")
            print("Thank you for ordering.")
            cart.clear()
            break

        elif confirm == "no":
            print("Order cancelled. Your cart is unchanged.")
            break

        else:
            print("Invalid input. Please enter yes or no.")


def main():
    menu = {
        "F101": {"name": "Pizza", "price": 250},
        "F102": {"name": "Burger", "price": 120},
        "F103": {"name": "Sandwich", "price": 80},
        "F104": {"name": "Fries", "price": 100},
        "F105": {"name": "Pasta", "price": 180}
    }

    cart = {}

    while True:
        print("\n===== FOOD ORDERING SYSTEM =====")
        print("1. Display Menu")
        print("2. Search Food")
        print("3. Add to Cart")
        print("4. Remove from Cart")
        print("5. View Cart")
        print("6. Calculate Bill")
        print("7. Place Order")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_menu(menu)

        elif choice == "2":
            search_food(menu)

        elif choice == "3":
            display_menu(menu)
            add_to_cart(menu, cart)

        elif choice == "4":
            remove_from_cart(menu, cart)

        elif choice == "5":
            view_cart(menu, cart)

        elif choice == "6":
            display_bill(menu, cart)

        elif choice == "7":
            place_order(menu, cart)

        elif choice == "8":
            print("Thank you for visiting.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
