# import module to print menu
import pymysql 

def products_menu():
    print ('''Enter
    0 to main menu,
    1 to print products from table,
    2 to create new products,
    3 to update existing product
    4 to delete product''')
    
def menu():
    while True:
        products_menu()
        menu_input = input('Enter choice \n')
        if menu_input == '0':
            # return to main_menu
            break
        elif menu_input== '1':
            '''def get_mysql_info():
    
            conn=pymysql.connect(host='localhost',user='root',passwd='password',db='Mazon-Kitchen')

            cursor = conn.cursor()
            cursor.execute ("SELECT * FROM products")
            all_rows = cursor.fetchall()
            
            # user input 1
            """for row in all_rows:
                print(f'Product_id: {str(row[0])}, name: {row[1]}, price: {row[2]}')"""
            
            # conn.close()
            
            # USER-INPUT 1
            """for row in all_rows:
                # print row header 
                print(row)
                print('\n')"""
    
get_mysql_info()'''
    
        elif menu_input== '2':
        # CREATE NEW PRODUCTS -  
            '''def create_new_product():
            try:
                conn=mysql.connector.connect(host='localhost',database='Mazon-Kitchen',user='root',password='password')
                
                cursor = conn.cursor()
                
                get_name = input('Enter name ')
                get_price =float((input('Enter price ')))
                
                sql_query = """INSERT INTO products (product_name, product_price) VALUES (%s,%s)"""
                record = (get_name,get_price)
                cursor.execute(sql_query,record)
                
                conn.commit()
                print("Record inserted successfully")
                # print(cursor.rowcount,'record inserted')
                
            except mysql.connector.Error as error:
                print("Failed to insert into MySQL table {}".format(error))

            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()
                    print("MySQL connection is closed")

        
create_new_product()'''
            pass
        
        elif menu_input== '3':
        # UPDATE EXISTING PRODUCT
            '''def get_mysql_info():
            
            conn=pymysql.connect(host='localhost',user='root',passwd='password',db='Mazon-Kitchen')

            cursor = conn.cursor()
            cursor.execute ("SELECT * FROM products")
            all_rows = cursor.fetchall()
            
            for row in all_rows:
                print(f'Product_id: {str(row[0])}, name: {row[1]}, price: {row[2]}')
            
            # ####### - get price 
            
            # prod_id = int(input('Enter product id\n'))
            # get_price =float((input('Enter price ')))
            # sql_query = """UPDATE products
            # SET product_price = %s
            # WHERE product_id = %s """
            # update_vals = (get_price,prod_id)
            
            # cursor.execute(sql_query, update_vals)
            # conn.commit()
            # print("Price Updated successfully ")
            
            
            #  ######## - get name 
            
            prod_id = int(input('Enter product id\n'))
            get_name =(input('Enter name\n'))
            
            # wrap in while loop 
            if get_name != "":
                sql_query = """UPDATE products
                SET product_name = %s
                WHERE product_id = %s """
                update_vals = (get_name,prod_id)

                cursor.execute(sql_query, update_vals)
                conn.commit()
                print("Name Updated successfully ")
            
            else:
                print('Try again')
            conn.close()
    
    # all: both name & price should I do that here too?
        
get_mysql_info()'''
            pass
        
        elif menu_input == '4':
        # DELETE PRODUCT
            '''def get_mysql_info():
    
        conn=pymysql.connect(host='localhost',user='root',passwd='password',db='Mazon-Kitchen')

        cursor = conn.cursor()
        cursor.execute ("SELECT * FROM products")
        all_rows = cursor.fetchall()
        
        for row in all_rows:
            print(f'Product_id: {str(row[0])}, name: {row[1]}, price: {row[2]}')
        
        prod_id = int(input('Enter product id\n'))
        del_product = """DELETE FROM products WHERE product_id = %s"""
        cursor.execute(del_product, (prod_id))
        conn.commit()
        print(f"Product {prod_id} successfully deleted ")

get_mysql_info()'''
            pass

menu()