from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token

import json

from tools.logging import logger

def handle_request():
    logger.debug("Get Products Handle Request")

    cursor = g.db.cursor()

    try:
        user_id = g.jwt_data['user_id']

        #select * from books;
        cursor.execute("select * from products;", user_id)
        print("Products Retrieved")
        
    except:
         print("Products unable to be found")
         return json_response(data={"message": "Products unable to be found."}, status=500)

     
    message = "{\"products\":["
    productCounter = 0
                 
    while True:
        db_row = cursor.fetchone()
                                 

        if db_row is None:
            print("No more products to add.")
            break;
        else:
            print("Adding Product...")
                                                                                 
            if productCounter > 0: message += ","
                                                                                 

            productCounter += 1
                                                                                                 
            #look at this in case of error, specifically product id
            message += "{\"company\": \"%s\", \"product\": \"%s\", \"price\": %s, \"product_id\": %s}" % (db_row[1], db_row[2], str(db_row[3]), str(db_row[0]))
            print("Product added.")
                                                                                                                                             
    message += "]}"
    print("The products were created.")
    return json_response(data=json.loads(message))
