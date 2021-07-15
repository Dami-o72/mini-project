
# Nigerian-Korean infusion restaurant

product_list = ['coke_zero','pepsi','velvet cake','bulgogi','kimchi','puffpuff']

main_menu = input('''      Enter 0 to exit, 
                           1 to print products list
                           2 to create new products
                           3 to update existing product
                           4 to delete product ''')

if main_menu == '0':
    print(main_menu) #how do you go back 
elif main_menu == '1' :
    print(product_list)
elif main_menu == '2':
    print('You are about to enter a new product')
    new_product = input('Enter new product: ')
    product_list.append(new_product)
    print (product_list)
elif main_menu == '3':
    pass #update existing products list
elif main_menu == '4':
    print(product_list)
    delete_product = input('Enter product you wish to delete: ')
    product_list.remove(delete_product)
    print(product_list)
    


