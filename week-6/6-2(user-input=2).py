# import module to print menu
import pymysql

def couriers_menu():
    print ('''Enter
    0 to main menu,
    1 to print couriers from table,
    2 to create new couriers,
    3 to update existing courier
    4 to delete courier''')
    
def menu():
    while True:
        couriers_menu()
        menu_input = input('Enter choice \n')
        if menu_input == '0':
            # return to main_menu
            break
        elif menu_input== '1':
            # get couriers from couriers table - TO DO
            # print couriers (done)
            '''def get_mysql_info():
    
    conn=pymysql.connect(host='localhost',user='root',passwd='password',db='Mazon-Kitchen')

    cursor = conn.cursor()
    cursor.execute ("SELECT * FROM couriers")
    all_rows = cursor.fetchall()
    
    # user input 1
    for row in all_rows:
        print(f'Courier_id: {str(row[0])}, name: {row[1]}, price: {row[2]}')
    
    # conn.close()
    
    # USER-INPUT 1
    """for row in all_rows:
        # print row header 
        print(row)
        print('\n')"""
    
get_mysql_info()'''
            
            pass
    
        elif menu_input== '2':
        # CREATE NEW couriers -  
            '''def create_new_product():
    try:
        conn=mysql.connector.connect(host='localhost',database='Mazon-Kitchen',user='root',password='password')
        
        cursor = conn.cursor()
        
        get_name = input('Enter name ')
        get_phone_number =int((input('Enter phone number ')))
        
        sql_query = """INSERT INTO  couriers (courier_name, phone_number) VALUES (%s,%s)"""
        record = (get_name,get_phone_number)
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
        # UPDATE EXISTING courier
            '''import pymysql

def get_mysql_info():
    
    conn=pymysql.connect(host='localhost',user='root',passwd='password',db='Mazon-Kitchen')

    cursor = conn.cursor()
    cursor.execute ("SELECT * FROM couriers")
    all_rows = cursor.fetchall()
    
    for row in all_rows:
        print(f'Courier_id: {str(row[0])}, name: {row[1]}, phone_number: {row[2]}')
    
    # ####### - get phone_number 
    
    cou_id = int(input("Enter product id\n"))
    get_phone_number =int((input("Enter phone_number ")))
    sql_query = """UPDATE couriers
    SET phone_number = %s
    WHERE courier_id = %s """
    update_vals = (get_phone_number,cou_id)
    
    cursor.execute(sql_query, update_vals)
    conn.commit()
    print("phone_number Updated successfully ")
    
    
    #  ######## - get name 
    # wrap HER in a while true <3
    cou_id = int(input('Enter courier id\n'))
    get_name =(input('Enter name\n'))
    
    # wrap in while loop 
    if get_name != "":
        sql_query = """UPDATE couriers
        SET courier_name = %s
        WHERE courier_id = %s """
        update_vals = (get_name,cou_id)

        cursor.execute(sql_query, update_vals)
        conn.commit()
        print("Name Updated successfully ")
    
    else:
        print("Try again")
    conn.close()
    
    # all: both name & phone_number should I do that here too?
        
get_mysql_info()'''
            pass
        
        elif menu_input == '4':
        # DELETE courier
    '''def get_mysql_info():
        
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

    get_mysql_info()'''
pass

menu()