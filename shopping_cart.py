import inventory
inventory_data=inventory.inventory_data
cart_data={}
total=0;

def add_to_cart(product_id,quantity,inventory_data):
    inventory.load_inventor()
    #print(inventory_data)
    if product_id in  inventory_data and quantity >0:
        if product_id not in cart_data :
            cart_data[product_id]={
                'quantity':quantity
            }
        else:
            cart_data[product_id]["quantity"]+=quantity
        
        if cart_data[product_id]['quantity'] <=inventory_data[product_id]['quantity']:
            print(f"product add to cart :Qunatity={quantity} ,name= {inventory_data[product_id]['name']}");
            #print(cart_data)
            return True
        else:
            cart_data[product_id]["quantity"]-=quantity
            print("insificient stcok ")
            return False

    else:
        print("invalid product or quantity \n")
        return False

def view_cart(cart_data, inventory_data):
    print("Shopping Cart:")
    #print(cart_data)
    
    for product_id, item in cart_data.items():
        try:
            product_name = inventory_data[product_id]['name']
            quantity = item['quantity']
            price = inventory_data[product_id]['price']
            print(f"Product: {product_name}, Quantity: {quantity}, Price: ${price:.2f}")
        except KeyError as e:
            print(f"Error: Product with ID {product_id} not found in inventory_data. Details: {e}")

def checkout(cart_data, inventory_data):
    print(f"Checkout process: ")
    total = 0  # Initialize total before the loop
    for product_id, item in cart_data.items():
        try:
            product_name = inventory_data[product_id]['name']
            quantity = item['quantity']
            price = inventory_data[product_id]['price']
            product_total = quantity * price
            #print(f"Product: {product_name}, Quantity: {quantity}")
            total += product_total  # Update total for each product
        except KeyError as e:
            print(f"Error: Product with ID {product_id} not found in inventory_data. Details: {e}")

    print(f"Total: ${total:.2f}")
    
    if(cart_data):
        for product_id, item in cart_data.items():
            inventory_data[product_id]['quantity'] -= item['quantity']

        inventory.save_inventory(inventory_data)
        cart_data.clear()
    else:
        print("empty cart data ")
