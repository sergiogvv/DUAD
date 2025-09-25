from flask import Flask, request, jsonify
from json import (load as jsonload, dump as jsondump, loads as jsonloads, dumps as jsondumps)
from os import path
from persistence import load_data, save_data
from datetime import datetime, timezone

status_list = ["pending", "in progress","complete"]
product_list_path= path.join(path.dirname(__file__), r'product_list.json')
error_log_path= path.join(path.dirname(__file__), r'errorlog.dat')


def validate_attributes_are_in_body(request_body):
    required_keys = ("id","title", "description", "status")
    for required_key in required_keys :
        if required_key not in request_body:
            raise ValueError(required_key+" is missing from the body")
    return True

def only_valid_attributes(request_body):
    allowed_keys = ("id", "title", "description", "status")
    for key in request_body.keys():
        if key not in allowed_keys:
            raise ValueError(f"Unexpected key in body: {key}")
    return True

def validate_no_empty_attributes(request_body):
    if str(request_body["id"]).strip() == "":
        raise ValueError("id can not be empty")
    if str(request_body["title"]).strip() == "":
        raise ValueError("title can not be empty")
    if str(request_body["description"]).strip() == "":
        raise ValueError("description can not be empty")
    if str(request_body["status"]).strip() == "":
        raise ValueError("status can not be empty")
    return True


def validate_product_id(request_body,product_id=None): # comprehensive id validation, can be used for POST or PUT
    product_list= load_data(product_list_path)
    for product in product_list:
        if request_body["id"] == product["id"]:
            if product_id == None:
                raise ValueError("id already exists")
            if product_id != str(request_body["id"]):
                print(product_id)
                print(request_body["id"])
                raise ValueError("id within request body already exists, please fill in request body id with a different value")
    return True


def save_json_product(request_body): #save product to json file
    product_list= load_data(product_list_path)
    product_list.append(request_body)
    json_products = jsondumps(product_list, indent=2)
    save_data(json_products, product_list_path)


def find_product_file_index(product_id): # used for PUT (pending test for PATCH) to find index for file to be updated
    product_list= load_data(product_list_path)
    for i in range(0,len(product_list)):
        if str(product_list[i]["id"]) == product_id:
            return i
    raise ValueError('Task not found')

def update_product_json(file_index,request_body):
    product_list= load_data(product_list_path)
    product_list[file_index] = request_body
    json_products = jsondumps(product_list, indent=2)
    save_data(json_products, product_list_path)


def delete_product_from_json(product_id): #delete product from json file
    product_list= load_data(product_list_path)
    for i in range(0,len(product_list)):
        if str(product_list[i]["id"]) == product_id:
            delete_product = product_list.pop(i)
            json_products = jsondumps(product_list, indent=2)
            save_data(json_products, product_list_path)
            return delete_product
    raise ValueError('Task not found')


def log_exception(ex): #log for debugging
    error_list= load_data(error_log_path)
    ex_log_dict = {
        "Exception": str(ex),
        "Time stamp": datetime.now(timezone.utc).isoformat()
    }
    error_list.append(ex_log_dict)
    json_string=jsondumps(error_list,indent=2)
    save_data(json_string,error_log_path)


def validate_status(request_body):
    if request_body["status"] not in status_list:
        raise ValueError("status not valid")
    return True


def api_response(data=None, message=""):
    return jsonify({
        "message": message,
        "data": data,
    })
