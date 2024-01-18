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


