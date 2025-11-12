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
    required_fields = ["full_name", "email", "username", "password", "DOB", "account_status"]
    missing = [field for field in required_fields if field not in request_body]
    if missing:
        raise ValueError(f"Missing fields: {', '.join(missing)}")
    return True

def is_valid_email(email):
    valid = re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)
    if not valid:
        raise ValueError('Invalid email format')
    return True

def is_valid_date(date_str):
    valid = datetime.strptime(date_str, "%Y-%m-%d")
    if not valid:
        raise ValueError('Invalid date format (use yyyy-mm-dd)') 
    return True

def is_valid_password(password):
    valid = len(password) >= 8 and any(c.isalpha() for c in password) and any(c.isdigit() for c in password)
    if not valid:
        raise ValueError("Password must be at least 8 characters and include letters and numbers")
    return True

def is_valid_username(username):
    valid = re.match(r'^\w+$', username)
    if not valid:
        raise ValueError("Username can only contain letters, numbers, and underscores")
    return True

def is_valid_account_status(account_status):
    allowed_status = ["ACTIVE", "INACTIVE", "DEFAULTED"]
    if account_status.upper() not in allowed_status:
        raise ValueError(f"Invalid status")
    return True

def check_email_duplicate(email, user_repo):
    existing_user = user_repo.get_by_email(email)
    if existing_user:
        raise ValueError('Email  already exists')

def check_result_success(result):
    if not result["success"]:
        raise ValueError(result["error"])
    return True

def validate_user_payload(request_body, user_repo):
    check_user_attributes(request_body)
    is_valid_email(request_body["email"])
    is_valid_date(request_body["DOB"])
    is_valid_password(request_body["password"])
    is_valid_username(request_body["username"])
    is_valid_account_status(request_body["account_status"])
    check_email_duplicate(request_body["email"], user_repo)

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

def is_valid_car_status(status):
    allowed_status = ["UNAVAILABLE", "AVAILABLE"]
    if status.upper() not in allowed_status:
        raise ValueError("Invalid status")
    return True

def check_rental_attributes(request_body):
    required_fields = ["car_id","user_id"]
    missing = [field for field in required_fields if field not in request_body]
    if missing:
        raise ValueError(f"Missing fields: {', '.join(missing)}")
    return True 

def check_if_user_id_exists(user_id, user_repo):
    existing_user = user_repo.get_by_id(user_id)
    if not existing_user:
        raise ValueError('User not found')
    
def check_if_user_id_active(user_id, user_repo):
    existing_user = user_repo.get_by_id(user_id)
    status = existing_user[0]["account_status"]
    if status != 'active':
        raise ValueError(f'User {user_id} is not {status}')
    
def check_if_car_available(car_id, car_repo):
    existing_car = car_repo.get_by_id(car_id)
    if not existing_car:
        raise ValueError('Car not found')
    status = existing_car[0]["status"]
    if status != "available":
        raise ValueError(f'Car {car_id} not available')

def validate_rental_payload(request_body, user_repo, car_repo):
    check_rental_attributes(request_body)
    check_if_user_id_exists(request_body["user_id"], user_repo)
    check_if_user_id_active(request_body["user_id"], user_repo)
    check_if_car_available(request_body["car_id"], car_repo)

def check_if_rental_id_exists(rental_id,rental_repo):
    existing_rental = rental_repo.get_by_id(rental_id)
    if not existing_rental:
        raise ValueError('Rental not found')   

def is_valid_rental_status(rental_status):
    allowed_status = ["RESERVED","IN USE", "RETURNED"]
    if rental_status.upper() not in allowed_status:
        raise ValueError("Invalid status")
    return True 

def valid_user_columns(column):
    VALID_COLUMNS = {"id", "full_name", "email", "username", "DOB", "account_status"}
    if column not in VALID_COLUMNS:
        raise ValueError(f"Invalid column: {column}")
    
def valid_car_columns(column):
    VALID_COLUMNS = {"id", "car_make", "model", "year","status"}
    if column not in VALID_COLUMNS:
        raise ValueError(f"Invalid column: {column}")

def valid_rental_columns(column):
    VALID_COLUMNS = {"id", "rental_date", "rental_status", "car_id","user_id"}
    if column not in VALID_COLUMNS:
        raise ValueError(f"Invalid column: {column}")