from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token


import json


from tools.logging import logger


def handle_request():
    logger.debug("Purchase Product Handle Request")

    cursor = g.db.cursor()


    try:
        cursor.execute("insert into purchased_products (user_id, product_id) VALUES (%s, %s);" % (str(g.jwt_data['user_id']), str(request.form['product_id']))) 
        g.db.commit()
        print("Product purchase was successful.")
        return json_response(data={"message": "You bought a product from the store!"})


    except:
        print("Unable to add purchased product.")
        return json_response(data={"message": "Unable to add/buy product"}, status=500)
