import inventory
import get_invenotory_data
inventory_data=get_invenotory_data.inventory_data;
i = 0
while i != 4:
    i = int(input('please enter the input: '))
    
    if i == 1:
        inventory.load_inventor()
        #print(inventory_data)
          
    elif i==2:
        inventory.save_inventory(inventory_data)
    elif i==3:
        print(inventory_data)
    else:
        break



#inventory.save_inventory(inventory_data)
#print(inventory_data)