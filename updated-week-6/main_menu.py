import products
import couriers
import orders
import csv
import pymysql


    
def main_menu():
    print ('''Enter
    1 to print products menu options,
    2 to print couriers menu options,
    3 to print orders menu options
    4 to exit''')
    
def menu():
    while True:
        main_menu()
        menu_input = input('Enter choice \n')
        if menu_input== '1':
            products.menu()
        elif menu_input== '2':
            couriers.menu()
        elif menu_input== '3':
            orders.menu()
        elif menu_input == '4':
            break
menu()