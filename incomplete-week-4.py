# user input 1 - print 
"""def print_list_or_dict(op): #change name 
    '''Print courier list, products list or orders dictionary'''
    print(op)

print_list_or_dict()"""

# user input 2 - create  -- rename to new_product/courier

"""def create(num:str):
    '''Create new product or new courier'''
    
    # product
    if num == '1':
        get_name = input('Enter name ')
        get_price = float(input('Enter price '))
    
    # new product
        product = {}
        product['name']= get_name.title()
        product['price'] = get_price
        # print (product)
        product_list.append(product)
        
        
    # courier
    elif num == '2':
        get_name = input('Enter name ')
        get_phone_number = input('Enter phone number ')
        
        # new courier
        courier = {}
        courier['name']= get_name.title()
        courier['price'] = get_phone_number
        # print (courier)
        courier_list.append(courier)
        print(courier_list)
        
create()"""

"""def create_order():
    '''Create new order'''
    
    print('You\'re about to create a new order')
    
    get_name = input('Enter full name ')
    get_customer_address = input('Enter customer address ')
    get_phone_number = input('Enter phone number ')
    
    for i, item in enumerate(products_list):
        print('\n',i,item)
    #this become the items     
    product_index_val = input('Enter index(es) of product with commas')
    list_of_int = list(map(int,product_index_val.split(',')))

    
    for i, item in enumerate(courier_list):
        print('\n',i,item)
    select_courier = input('Enter index of courier ')
    order_status = 'PREPARING'
    
    orders_dict["customer_name"] = get_name
    orders_dict["customer_address"] = get_customer_address
    orders_dict["customer_phone"] = get_phone_number
    orders_dict["courier"] = select_courier
    orders_dict["status"] = order_status
    orders_dict["items"] = list_of_int
    
    print(orders_dict)

    orders_list.append(orders_dict)
    
create_order()
"""
# user input 4 - delete 
"""def delete_list(menu_list):
    '''Delete product, courier or orders list'''
    for i, item in enumerate(menu_list):
        print('\n',i,item)
    delete_product = input('would you like to delete product? y/n\n ')
        
    if delete_product == 'y':
        index_2 = int(input('Enter index\n'))
        remove = menu_list.pop(index_2)
        print(menu_list)
        
        # make robust by ensuring user has entered right index list and right value into input
    
delete_list(product_list)"""

