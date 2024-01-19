
inventory_data = {}
def load_inventor():
    try:
        
        file= open('inventory_data.txt', 'r') 
        next(file);
        for line in file:
            product_id, name, price, quantity = line.strip().split(',')
            #print(product_id,name,price,quantity)
            inventory_data[int(product_id)]={
                'name': name,
                'price': float(price),
                'quantity': int(quantity)
            }
        #print(get_invenotory_data.inventory_data)
            #print(inventory_data)
        file.close()
    except FileNotFoundError:
        print("The file does not exist.")
    except Exception as e:
         print(f"An error occurred: {e}")


def save_inventory(inventory_data):
    try:
        # inventory_data[104]={
        #     'name': 'Laptop', 'price': 800.0, 'quantity': 10
        # }
        #print(inventory_data)
        file= open('inventory_data.txt', 'w')
        file.write("ProductID,Name,Price,Quantity\n")
        for product_id, product_info in inventory_data.items():
             line = f"{product_id},{product_info['name']},{product_info['price']},{product_info['quantity']}\n"
             file.write(line)
        print(f"Inventory data saved to file\n")
        file.close()
    except Exception as e:
         print(f"An error occurred: {e}")
    
def add_product(product_id,name,price,quantity,inventory_data):
    inventory_data[int(product_id)]={
        'name': name,
        'price': float(price),
        'quantity': int(quantity)
    }
    print(inventory_data)
    save_inventory(inventory_data)
    print("add inventory ");
    
def update_stcok(product_id,quantity_change,inventory_data):
    if product_id in inventory_data:
        inventory_data[product_id]['quantity']+=quantity_change;
        save_inventory(inventory_data)
        print(inventory_data)
        
    else:
        print("id not found ")


def view_inventory():
    if inventory_data:
        for product_id, item in inventory_data.items():
            try:
                product_name = inventory_data[product_id]['name']
                quantity = inventory_data[product_id]['quantity']
                price = inventory_data[product_id]['price']
                print(f"Product: {product_name}, Quantity: {quantity}, Price: ${price}")
            except KeyError as e:
                print(f"Error: something wromng")
    else:
        print('empty \n')
