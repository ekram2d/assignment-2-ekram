import inventory
import shopping_cart
import payment

inventory_data = inventory.inventory_data
cart_data = shopping_cart.cart_data
total = shopping_cart.total

i = 0

while True:
    try:
        inventory.load_inventor()

        print("Please enter 1 to view inventory")
        print("Please enter 2 to add products to the cart")
        print("Please enter 3 to view the cart")
        print("Please enter 4 to checkout")
        print("Please enter 0 to exit")

        i = int(input("Enter your choice: "))

        if i == 1:
            inventory.view_inventory()

        elif i == 2:
            product_id = int(input("Please enter the product_id: "))
            quantity = int(input('Please enter the quantity: '))
            shopping_cart.add_to_cart(product_id, quantity, inventory_data)

        elif i == 3:
            shopping_cart.view_cart(cart_data, inventory_data)

        elif i == 4:
            shopping_cart.checkout(cart_data, inventory_data)
        elif i==5:
            payment.process_payment(10)

        elif i == 0:
            break

        else:
            print("Invalid choice. Please enter a valid option.")

    except ValueError as ve:
        print(f"Error: {ve}. Please enter a valid numeric input.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

