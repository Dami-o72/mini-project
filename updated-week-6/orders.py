import pymysql
import csv


def orders_menu():
    print ('''Enter
    0 to main menu,
    1 to print orders from table and load to csv,
    2 to create new orders,
    3 to update order status
    4 to update existing order
    5 to delete order''')

def menu():
    while True:
        orders_menu()
        menu_input = input('Enter choice \n')
        if menu_input == '0':
            break
        
        elif menu_input == '1':
        
            def get_mysql_info():
                try:    
                    conn=pymysql.connect(host='localhost',user='root',passwd='password',db='Mazon-Kitchen')

                    cursor = conn.cursor()
                    cursor.execute ("SELECT * FROM orders")
                    all_rows = cursor.fetchall()
                    
                    
                    for row in all_rows:
                        print(
                            f'customer_id: {str(row[0])}, name: {row[1]}, address: {row[2]},phone number: {row[3]},courier: {row[4]},status: {row[5]},items: {row[6]}  \n')
                except pymysql.connector.Error as e:
                    print("Error printing data from MySQL table", e)
                
                finally:
                    conn.close()
                    return all_rows
                    print("MySQL connection is closed")
            
            def write_csv():
                data = get_mysql_info()
                filename = 'orders.csv'
                with open(filename,mode='w',encoding='utf-8') as f: 
                    write = csv.writer(f,dialect='excel')
                    for item in data:
                        write.writerow(item)
        
            write_csv() 
            break

        elif menu_input == '2':
            
            def create_new_order():
                try:
                    conn=pymysql.connect(host='localhost',database='Mazon-Kitchen',user='root',password='password')
                    
                    cursor = conn.cursor()
                    
                    get_name = input('Enter full name ').title()
                    get_customer_address = input('Enter customer address ')
                    get_phone_number = input('Enter phone number ')
                    
                    cursor.execute ("SELECT * FROM products")
                    all_rows = cursor.fetchall()
                    for row in all_rows:
                        print(f'Product_id: {str(row[0])}, name: {row[1]}, price: {row[2]}')
                    
                    product_index_val = input('Enter index(es) of product with commas\n')
                    
                    cursor.execute ("SELECT * FROM couriers")
                    all_rows = cursor.fetchall()
                    for row in all_rows:
                        print(f'Courier_id: {str(row[0])}, name: {row[1]}, price: {row[2]}')
                        
                    select_courier = input('Enter index of courier ')
                    
                    statuses = 1
                    
                    sql_query = """INSERT INTO orders(customer_name,customer_address,customer_phone_number,courier,statuses,items) VALUES (%s,%s,%s,%s,%s,%s)"""
                    record = (get_name,get_customer_address,get_phone_number,select_courier,statuses,product_index_val)
                    cursor.execute(sql_query,record)
                    
                    conn.commit()
                    print("Record inserted successfully")
                    # print(cursor.rowcount,'record inserted')
                    
                except pymysql.connector.Error as error:
                    print("Failed to insert into MySQL table {}".format(error))

                finally:
                        cursor.close()
                        conn.close()
                        print("MySQL connection is closed")

            create_new_order()
            break
        
        elif menu_input == '3':
            def update_order_status():
                try:
                    conn=pymysql.connect(host='localhost',user='root',passwd='password',db='Mazon-Kitchen')

                    
                    cursor = conn.cursor()
                    cursor.execute ("SELECT * FROM orders")
                    all_rows = cursor.fetchall()
                    
                    for row in all_rows:
                        print(
                            f'customer_id: {str(row[0])}, name: {row[1]}, address: {row[2]},phone number: {row[3]},courier: {row[4]},status: {row[5]},items: {row[6]}\n')  
                        
                    cursor.execute("SELECT customer_id, customer_name, statuses FROM orders")
                    all_rows = cursor.fetchall()
                    
                    for row in all_rows:
                        print(f'customer_id:{str(row[0])},name: {row[1]},status: {row[2]}\n')
                    
                    print(""" Order Status List:
                    When prompted enter:
                    1 to update order status to PREPARING
                    2 to update to WITH COURIER
                    3 to update to DELIVERED      
                        """)
                    
                    get_order_id = input('Enter customer order id ')
                    order_index_value = int(input('Enter index from order status list to update status of order\n'))
                    
                    sql_query = """UPDATE orders
                    SET statuses = %s
                    WHERE customer_id = %s """
                    update_vals = (order_index_value,get_order_id)
                    
                    
                    cursor.execute(sql_query, update_vals)
                    conn.commit()
                    print("Status updated successfully ")
                
                except pymysql.connector.Error as error:
                    print("Failed to update values: {update_vals}".format(error))
                finally:
                    conn.close()
                    print("MySQL connection is closed")

            update_order_status()
            break
        
        elif menu_input == '4':
            
            def update_order():
                try:
                    conn=pymysql.connect(host='localhost',user='root',passwd='password',db='Mazon-Kitchen')

                    cursor = conn.cursor()
                    cursor.execute ("SELECT * FROM orders")
                    all_rows = cursor.fetchall()
                    for row in all_rows:
                        print(f'customer_id: {str(row[0])}, name: {row[1]}, address: {row[2]},phone number: {row[3]},courier: {row[4]},status: {row[5]},items: {row[6]}\n')
                    
                    get_order_id = input('Enter customer order id ')
                    get_name = input('Enter full name ').title()
                    get_customer_address = input('Enter customer address ')
                    get_phone_number = input('Enter phone number ')
                    
                    
                    cursor.execute ("SELECT * FROM products")
                    all_rows = cursor.fetchall()
                    for row in all_rows:
                        print(f'Product_id: {str(row[0])}, name: {row[1]}, price: {row[2]}\n')
                    
                    # user input for product id
                    product_index_val = input('Enter index(es) of product with commas\n')
                    
                    cursor.execute ("SELECT * FROM couriers")
                    all_rows = cursor.fetchall()
                    for row in all_rows:
                        print(f'Courier_id: {str(row[0])}, name: {row[1]}, phone_number: {row[2]}\n')
                    
                    # user input for courier id
                    cou_id = int(input("Enter courier id\n"))
                    
                    sql_query = """UPDATE orders
                    SET customer_name = %s, customer_address = %s, customer_phone_number = %s, courier = %s, items = %s
                    WHERE customer_id = %s """
                    update_vals = (get_name,get_customer_address,get_phone_number, cou_id,product_index_val,get_order_id)
                    
                    cursor.execute(sql_query, update_vals)
                    conn.commit()
                    print("multiple records updated successfully ")
                    
                except pymysql.connector.Error as error:
                    print("Failed to update values: {update_vals}".format(error))
                finally:
                    conn.close()
                    print("MySQL connection is closed")
        
            update_order()
            break
    
        elif menu_input == '5':
            def delete_order():
                try:
                    conn=pymysql.connect(host='localhost',user='root',passwd='password',db='Mazon-Kitchen')

                    cursor = conn.cursor()
                    cursor.execute ("SELECT * FROM orders")
                    all_rows = cursor.fetchall()
                    
                    for row in all_rows:
                        print(
                            f'customer_id: {str(row[0])}, name: {row[1]}, address: {row[2]},phone number: {row[3]},courier: {row[4]},status: {row[5]},items: {row[6]} ')
                    
                    cust_id = int(input('Enter customer id\n'))
                    del_order = """DELETE FROM orders WHERE customer_id = %s"""
                    cursor.execute(del_order, (cust_id))
                    conn.commit()
                    print(f"order {cust_id} successfully deleted ")

                except pymysql.connector.Error as error:
                    print("Failed to delete record from table: {cust_id}".format(error))
                finally:
                    conn.close()
                    print("MySQL connection is closed")
            delete_order()
            break

        
