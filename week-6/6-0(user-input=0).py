    
def main_menu():
    print ('''Enter
    0 to save list to csv file,
    1 to print products menu options,
    2 to print couriers menu options,
    3 to print orders menu options''')
    
def menu():
    while True:
        main_menu()
        menu_input = input('Enter choice \n')
        if menu_input == '0':
            print('load data + save to csv')
            # load data/list from DB
            # save it to csv file 
            break
        elif menu_input== '1':
            print('print product menu options')
            # print product menu options
            # else or elif products_menu == 0:
                # print main_menu options
            pass
    
        elif menu_input== '2':
            print('print courier menu options')
            # print courier menu options
            pass
        
        elif menu_input== '3':
            print('print order menu options')
            # print orders menu options
            pass

menu()