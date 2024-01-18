import get_invenotory_data
def load_inventor():
    try:
        
        file= open('inventory_data.txt', 'r') 
        next(file);
        for line in file:
            product_id, name, price, quantity = line.strip().split(',')
            #print(product_id,name,price,quantity)
            get_invenotory_data.inventory_data[int(product_id)]={
                'name': name,
                'price': float(price),
                'quantity': int(quantity)
            }
        #print(get_invenotory_data.inventory_data)
        file.close()
    except FileNotFoundError:
        print("The file does not exist.")
    except Exception as e:
         print(f"An error occurred: {e}")


def save_inventory(inventory_data):
    try:
        inventory_data[104]={
            'name': 'Laptop', 'price': 800.0, 'quantity': 10
        }
        print(inventory_data)
        file= open('inventory_data.txt', 'w')
        file.write("ProductID,Name,Price,Quantity\n")
        for product_id, product_info in inventory_data.items():
             line = f"{product_id},{product_info['name']},{product_info['price']},{product_info['quantity']}\n"
             file.write(line)
        print(f"Inventory data saved to file\n")
    except Exception as e:
         print(f"An error occurred: {e}")
    
    
    



