from json import (load as jsonload, dump as jsondump, loads as jsonloads, dumps as jsondumps)
import re
from datetime import datetime, timezone
from flask import Flask, request, jsonify
from json import (load as jsonload, dump as jsondump, loads as jsonloads, dumps as jsondumps)



def api_response(data=None, message=""):
    return jsonify({
        "data": data,
        "message": message,
    })

def check_user_attributes(request_body):
    required_fields = ["full_name", "user_name", "password"]
    missing = [field for field in required_fields if field not in request_body]
    if missing:
        raise ValueError(f"Missing fields: {', '.join(missing)}")
    return True

def is_valid_password(password):
    valid = len(password) >= 8 and any(c.isalpha() for c in password) and any(c.isdigit() for c in password)
    if not valid:
        raise ValueError("Password must be at least 8 characters and include letters and numbers")
    return True

def is_valid_username(user_name):
    valid = re.match(r'^\w+$', user_name)
    if not valid:
        raise ValueError("Username can only contain letters, numbers, and underscores")
    return True

def check_result_success(result):
    if not result["success"]:
        raise ValueError(result["error"])
    return True

def validate_user_payload(request_body, user_repo):
    check_user_attributes(request_body)
    is_valid_password(request_body["password"])
    is_valid_username(request_body["user_name"])

def check_car_attributes(request_body):
    required_fields = ["car_make", "model", "year"]
    missing = [field for field in required_fields if field not in request_body]
    if missing:
        raise ValueError(f"Missing fields: {', '.join(missing)}")
    return True 

def check_if_car_id_exists(car_id, car_repo):
    existing_car = car_repo.get_by_id(car_id)
    if not existing_car:
        raise ValueError('Car not found')

def check_if_car_exists(column, value, car_repo):
    existing_car = car_repo.get_by_column(column,value)
    if not existing_car:
        raise ValueError('Car not found')    

def check_address_attributes(request_body):
    required_fields = ["user_id","address"]
    missing = [field for field in required_fields if field not in request_body]
    if missing:
        raise ValueError(f"Missing fields: {', '.join(missing)}")
    return True 

def check_if_user_id_exists(user_id, user_repo):
    existing_user = user_repo.get_by_id(user_id) 
    if not existing_user:
        raise ValueError('User not found')

def check_if_user_exists(column, value, user_repo):
    existing_user = user_repo.get_by_column(column,value)
    if not existing_user:
        raise ValueError('User not found')

def check_if_address_exists(column, value, address_repo):
    existing_address = address_repo.get_by_column(column,value)
    if not existing_address:
        raise ValueError('User not found')

def validate_address_payload(request_body, user_repo):
    check_address_attributes(request_body)
    check_if_user_id_exists(request_body["user_id"], user_repo)

# def check_if_rental_id_exists(rental_id,rental_repo):
#     existing_rental = rental_repo.get_by_id(rental_id)
#     if not existing_rental:
#         raise ValueError('Rental not found')   

# def is_valid_rental_status(rental_status):
#     allowed_status = ["RESERVED","IN USE", "RETURNED"]
#     if rental_status.upper() not in allowed_status:
#         raise ValueError("Invalid status")
#     return True 

def valid_user_columns(column):
    VALID_COLUMNS = {"id", "full_name", "user_name", "password"}
    if column not in VALID_COLUMNS:
        raise ValueError(f"Invalid column: {column}")
    
def valid_car_columns(column):
    VALID_COLUMNS = {"id", "car_make", "model", "year"}
    if column not in VALID_COLUMNS:
        raise ValueError(f"Invalid column: {column}")

def valid_address_columns(column):
    VALID_COLUMNS = {"id", "user_id", "address"}
    if column not in VALID_COLUMNS:
        raise ValueError(f"Invalid column: {column}")