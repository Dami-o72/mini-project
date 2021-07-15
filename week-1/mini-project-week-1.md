# Mini Project Week 1

In this week we'll be building out the foundation of your app, in particular, the UI aspect.
This will make use of your ability to print to the screen, clear the screen, accept user input, and create a basic `list` data structure.

Try to make good use of functions for repetitive tasks.

## Goals

As a user I want to:

- create a product and add it to a list
- view all products
- _STRETCH_ update or delete a product

## Spec

A `product` should just be a `string` containing its name, i.e: `"Coke Zero"`
A list of `products` should be a list of `strings`, i.e: ` Products_list = ["Coke Zero"]` #to access it for example use: for product (above) in products_list

## Pseudo Code

```txt
# add some product names
CREATE products list

PRINT main menu options
GET user input for main menu option

IF user input is 0: #main menu option here - allows customer to choose what they would like to do 
    EXIT app

# products menu
ELSE IF user input is 1: #main menu options 

    PRINT product menu options
    GET user input for product menu option

    IF user input is 0:
        RETURN to main menu

    ELSE IF user input is 1: #done
        PRINT products list

    ELSE IF user input is 2: #done

        # CREATE new product
        GET user input for product name
        APPEND product name to products list

    ELSE IF user input is 3: #need this to be expanded upon - how is this different to the above 
    
        # STRETCH GOAL - UPDATE existing product
        PRINT product names with its index value 
        for product in product_list:
            print(product, index)
        GET user input for product index value #product_list[i]
        GET user input for new product name
        UPDATE product name at index in products list

    ELSE IF user input is 4:

        # STRETCH GOAL - DELETE product
        PRINT products list
        GET user input for product index value # first print product index
        #then print product

        #use for loop to print index of product e.g. 
        for i in products_list:
            if i == (?)
            print(products_list(index))
            del_product = input('Enter product you want to delete') 
        DELETE product at index in products list 
```
