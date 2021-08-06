import pymysql 
import csv


def products_menu():
    print ('''Enter
    0 to main menu,
    1 to print products from table and load to csv,
    2 to create new products,
    3 to update existing product
    4 to delete product''')
    
def menu():
    while True:
        products_menu()
        menu_input = input('Enter choice \n')
        if menu_input == '0':
            break
        
        elif menu_input== '1':
            def get_mysql_info():
                '''Print products list and save to csv file'''
                try:    
                    conn=pymysql.connect(host='localhost',user='root',passwd='password',db='Mazon-Kitchen')

                    cursor = conn.cursor()
                    cursor.execute ("SELECT * FROM products")
                    all_rows = cursor.fetchall()
                    
                    for row in all_rows:
                        print(f'Product_id: {str(row[0])}, name: {row[1]}, price: {row[2]}\n')
                
                except pymysql.connector.Error as e:
                    print("Error printing data from MySQL table", e)
                
                finally:
                    conn.close()
                    return all_rows
                    print("MySQL connection is closed")
                
            def write_csv():
                data = get_mysql_info()
                filename = 'products.csv'
                with open(filename,mode='w',encoding='utf-8') as f: 
                    write = csv.writer(f,dialect='excel')
                    for item in data:
                        write.writerow(item)
        
            write_csv()
            break

        elif menu_input== '2':
            
            def create_new_product():
                '''Create new product'''
                try:
                    
                    conn=pymysql.connect(host='localhost',database='Mazon-Kitchen',user='root',password='password')
                    cursor = conn.cursor()
                    
                    get_name = input('Enter name ')
                    get_price =float((input('Enter price ')))
                    
                    sql_query = """INSERT INTO products (product_name, product_price) VALUES (%s,%s)"""
                    record = (get_name,get_price)
                    cursor.execute(sql_query,record)
                    
                    conn.commit()
                    print("Record inserted successfully")
                    
                    
                except pymysql.connector.Error as error:
                    print("Failed to insert into MySQL table {}".format(error))

                finally:
                        conn.close()
                        print("MySQL connection is closed")

            create_new_product()
            break
        
        elif menu_input== '3':
            
            def update_product():
                """Update existing product"""
                
                conn=pymysql.connect(host='localhost',user='root',passwd='password',db='Mazon-Kitchen')

                cursor = conn.cursor()
                cursor.execute ("SELECT * FROM products")
                all_rows = cursor.fetchall()
                
                for row in all_rows:
                    print(f'Product_id: {str(row[0])}, name: {row[1]}, price: {row[2]}')
                    
                update_input = input("Enter 'name' to update name,\
                                    'price' to update price  and \
                                    'all' to update both \n")    
                
                if update_input == 'name':
                    
                    prod_id = int(input('Enter product id\n'))
                    get_name =(input('Enter name\n')).title()
            
                    if get_name != "":
                        sql_query = """UPDATE products
                        SET product_name = %s
                        WHERE product_id = %s """
                        update_vals = (get_name.title(),prod_id)

                        cursor.execute(sql_query, update_vals)
                        conn.commit()
                        print("Name Updated successfully ")
                    
                    else:
                        print('Try again')
                
                elif update_input == 'price':
                    
                    prod_id = int(input('Enter product id\n'))
                    get_price =float((input('Enter price ')))
                    
                    if get_price != "":
                        sql_query = """UPDATE products
                        SET product_price = %s
                        WHERE product_id = %s """
                        update_vals = (get_price,prod_id)
                        
                        cursor.execute(sql_query, update_vals)
                        conn.commit()
                        print("Price Updated successfully ")
                
                elif update_input == 'all':
                    
                    prod_id = int(input('Enter product id\n'))
                    get_name =(input('Enter name\n')).title()
                    sql_query = """UPDATE products
                    SET product_name = %s
                    WHERE product_id = %s """
                    update_vals = (get_name.title(),prod_id)

                    cursor.execute(sql_query, update_vals)
                    conn.commit()
                    print("Name Updated successfully ")
                    
                    prod_id = int(input('Enter product id\n'))
                    get_price =float((input('Enter price ')))
                    sql_query = """UPDATE products
                    SET product_price = %s
                    WHERE product_id = %s """
                    update_vals = (get_price,prod_id)
                    
                    cursor.execute(sql_query, update_vals)
                    conn.commit()
                    print("Price Updated successfully ")

            update_product()
            break
            
        elif menu_input == '4':
            
            def del_product():
                '''Delete a product'''
                try:
                    conn=pymysql.connect(host='localhost',user='root',passwd='password',db='Mazon-Kitchen')

                    cursor = conn.cursor()
                    cursor.execute ("SELECT * FROM products")
                    all_rows = cursor.fetchall()
                    
                    for row in all_rows:
                        print(f'Product_id: {str(row[0])}, name: {row[1]}, price: {row[2]}')
                    
                    prod_id = int(input('Enter product id\n'))
                    del_prod = """DELETE FROM products WHERE product_id = %s"""
                    cursor.execute(del_prod, (prod_id))
                    conn.commit()
                    print(f"Product {prod_id} successfully deleted ")
                
                except pymysql.connector.Error as error:
                    print("Failed to delete record from table: {prod_id}".format(error))
                finally:
                    conn.close()
                    print("MySQL connection is closed")

            del_product()
            break    

        

        
        