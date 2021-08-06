import pymysql
import csv


def couriers_menu():
    print ('''Enter
    0 to main menu,
    1 to print couriers from table and load to csv,
    2 to create new couriers,
    3 to update existing courier
    4 to delete courier''')
    
def menu():
    while True:
        couriers_menu()
        menu_input = input('Enter choice \n')
        if menu_input == '0':
            break
        
        elif menu_input== '1':
            def get_mysql_info():
                try:
                    conn=pymysql.connect(host='localhost',user='root',passwd='password',db='Mazon-Kitchen')

                    cursor = conn.cursor()
                    cursor.execute ("SELECT * FROM couriers")
                    all_rows = cursor.fetchall()
                    
                    for row in all_rows:
                        print(f'Courier_id: {str(row[0])}, name: {row[1]}, phone_number: {row[2]}\n')
                except pymysql.connector.Error as e:
                    print("Error printing data from MySQL table", e)
                
                finally:
                    conn.close()
                    return all_rows
                    print("MySQL connection is closed")
            
            def write_csv():
                data = get_mysql_info()
                filename = 'couriers.csv'
                with open(filename,mode='w',encoding='utf-8') as f: 
                    write = csv.writer(f,dialect='excel')
                    for item in data:
                        write.writerow(item)
        
            write_csv() 
            break
        
        elif menu_input== '2':
            
            def create_new_courier():
                try:
                    conn=pymysql.connect(host='localhost',database='Mazon-Kitchen',user='root',password='password')
                    
                    cursor = conn.cursor()
                    
                    get_name = input('Enter name ').title()
                    get_phone_number =(input('Enter phone number '))
                    
                    sql_query = """INSERT INTO  couriers (courier_name, phone_number) VALUES (%s,%s)"""
                    record = (get_name,get_phone_number)
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
            
            create_new_courier()
            break
        
        elif menu_input == '3':
            
            def update_courier():
                conn=pymysql.connect(host='localhost',user='root',passwd='password',db='Mazon-Kitchen')

                cursor = conn.cursor()
                cursor.execute ("SELECT * FROM couriers")
                all_rows = cursor.fetchall()
                
                for row in all_rows:
                    print(f'Courier_id: {str(row[0])}, name: {row[1]}, phone_number: {row[2]}\n')
                
                update_input = input("Enter 'name' to update name,\
                                    'price' to update price  and \
                                    'all' to update both \n")    
                
                if update_input == 'name':
                    
                    cou_id = int(input('Enter courier id\n'))
                    get_name =(input('Enter name\n')).title()
            
                    if get_name != "":
                        sql_query = """UPDATE couriers
                        SET courier_name = %s
                        WHERE courier_id = %s """
                        update_vals = (get_name,cou_id)

                        cursor.execute(sql_query, update_vals)
                        conn.commit()
                        print("Name Updated successfully ")
                    
                    else:
                        print('Try again')
                
                elif update_input == 'phone_number':
                    
                    cou_id = int(input("Enter courier id\n"))
                    get_phone_number =int((input("Enter phone_number ")))
                    
                    if get_phone_number != "":
                        sql_query = """UPDATE couriers
                        SET phone_number = %s
                        WHERE courier_id = %s """
                        update_vals = (get_phone_number,cou_id)
                        
                        cursor.execute(sql_query, update_vals)
                        conn.commit()
                        print("Phone_number updated successfully ")
                
                elif update_input == 'all':
                    
                    cou_id = int(input('Enter courier id\n'))
                    get_name =(input('Enter name\n')).title()

                    sql_query = """UPDATE couriers
                    SET courier_name = %s
                    WHERE courier_id = %s """
                    update_vals = (get_name,cou_id)

                    cursor.execute(sql_query, update_vals)
                    conn.commit()
                    print("Courier name updated successfully ")
                    
        
                    cou_id = int(input("Enter courier id\n"))
                    get_phone_number =int((input("Enter phone_number ")))
                    sql_query = """UPDATE couriers
                    SET phone_number = %s
                    WHERE courier_id = %s """
                    update_vals = (get_phone_number,cou_id)
                    
                    cursor.execute(sql_query, update_vals)
                    conn.commit()
                    print("Phone_number updated successfully ")
            
            update_courier()
            break
        
        elif menu_input == '4':
            
            def delete_courier():
                try:
                    conn=pymysql.connect(host='localhost',user='root',passwd='password',db='Mazon-Kitchen')

                    cursor = conn.cursor()
                    cursor.execute ("SELECT * FROM couriers")
                    all_rows = cursor.fetchall()
                    
                    for row in all_rows:
                        print(f'Courier_id: {str(row[0])}, name: {row[1]}, price: {row[2]}')
                    
                    coud_id = int(input('Enter courier id\n'))
                    del_courier = """DELETE FROM couriers WHERE courier_id = %s"""
                    cursor.execute(del_courier, (coud_id))
                    conn.commit()
                    print(f"courier {coud_id} successfully deleted ")
                
                except pymysql.connector.Error as error:
                    print("Failed to delete record from table: {coud_id}".format(error))
                finally:
                    conn.close()
                    print("MySQL connection is closed")

            delete_courier()
            break

    