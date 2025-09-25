from flask import Flask, request, jsonify
from os import path
from persistence import load_data, save_data
from utilities import find_product_file_index, api_response, only_valid_attributes, log_exception,validate_attributes_are_in_body, validate_no_empty_attributes, validate_product_id, save_json_product, validate_status, delete_product_from_json, update_product_json, product_list_path

app = Flask(__name__)


#CREATE
@app.route("/product", methods = ["POST"])
def create_product():
    try:
        request_body = request.json
        #validations
        only_valid_attributes(request_body) #body can only contain valid attributes 
        validate_attributes_are_in_body(request_body)
        validate_no_empty_attributes(request_body)
        validate_product_id(request_body)
        validate_status(request_body)
        #save product to json file
        save_json_product(request_body)
        return api_response(request_body,"Added data")
    except ValueError as ex:
        log_exception(ex) #log errors in file
        return api_response(message= str(ex)), 400
    except Exception as ex:
        log_exception(ex) #log errors in file
        return api_response(message= "Unexpected error"), 500 #unexpected generic error with generic message

#READ
@app.route("/product", methods = ["GET"])
def read_product():
    try:
        filtered_product_list= load_data(product_list_path) #Load data (product_list)
        status_filter = request.args.get("status")
        if status_filter:
            filtered_product_list = list(
                filter(lambda product: product["status"] == status_filter.lower(), filtered_product_list) #lower case for added flexibility for the user
            )
        return api_response(filtered_product_list,"product list")
    except ValueError as ex:
        log_exception(ex) #log errors in file
        return api_response(message= str(ex)), 400
    except Exception as ex:
        log_exception(ex) #log errors in file
        return api_response(message= "Unexpected error"), 500 #unexpected generic error with generic message    

#UPDATE
@app.route("/product/<product_id>", methods = ["PUT"])
def update_product(product_id):
    try:
        request_body = request.json
        #validations
        file_index = find_product_file_index(product_id) #returns error if product_id is not found
        validate_attributes_are_in_body(request_body)
        validate_no_empty_attributes(request_body)
        validate_status(request_body)
        validate_product_id(request_body,product_id) #returns error only if product id is being updated to a value that already exists
        
        update_product_json(file_index,request_body) 
        return api_response(request_body,"Update data")
    except ValueError as ex:
        log_exception(ex) #log errors in file
        return api_response(message= str(ex)), 400
    except Exception as ex:
        log_exception(ex) #log errors in file
        return api_response(message= "Unexpected error"), 500 #unexpected generic error with generic message     

#DELETE
@app.route("/product/<product_id>", methods = ["DELETE"])
def delete_product(product_id):
    try:
        delete_product = delete_product_from_json(product_id)
        return api_response(delete_product,"Deleted data")
    except ValueError as ex:
        log_exception(ex) #log errors in file
        return api_response(message= str(ex)), 400
    except Exception as ex:
        log_exception(ex) #log errors in file
        return api_response(message= "Unexpected error"), 500 #unexpected generic error with generic message 










