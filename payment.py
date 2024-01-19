import shopping_cart
import inventory
def process_payment(amount):
    #print(shopping_cart.cart_data)
    try:
        x = input("Do you want to make a payment? yes or no: ")
        if x.lower() == 'yes':
            mobile = input("Enter your mobile number: ")
            transaction_id = input("Enter your transaction id: ")
            cart_data = shopping_cart.cart_data
            print(f'Payment successful! Mobile: {mobile}, Transaction ID: {transaction_id}, Amount: {amount}')
            if(cart_data):
                for product_id, item in cart_data.items():
                    inventory.inventory_data[product_id]['quantity'] -= item['quantity']
                    inventory.save_inventory(inventory.inventory_data)
                    cart_data.clear()
            else:
               print("empty cart data ")
            return True
        else:
            print("See you soon!")
            return False
    except Exception as e:
        print(f"An error occurred during payment: {e}")
        return False
