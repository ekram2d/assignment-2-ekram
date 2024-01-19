import shopping_cart

def process_payment(amount):
    try:
        x = input("Do you want to make a payment? yes or no: ")
        if x.lower() == 'yes':
            mobile = input("Enter your mobile number: ")
            transaction_id = input("Enter your transaction id: ")
            cart_data = shopping_cart.cart_data
            print(f'Payment successful! Mobile: {mobile}, Transaction ID: {transaction_id}, Amount: {amount}')
            cart_data.clear()
            return True
        else:
            print("See you soon!")
            return False
    except Exception as e:
        print(f"An error occurred during payment: {e}")
        return False
