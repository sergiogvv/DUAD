from flask import Flask, request, jsonify
from os import path
from persistence import load_data, save_data
from utilities import find_task_file_index, api_response, only_valid_attributes, log_exception,validate_attributes_are_in_body, validate_no_empty_attributes, validate_task_id, save_json_task, validate_status, delete_task_from_json, update_task_json, task_list_path

app = Flask(__name__)


#CREATE
@app.route("/task", methods = ["POST"])
def create_task():
    try:
        request_body = request.json
        #validations
        only_valid_attributes(request_body) #body can only contain valid attributes 
        validate_attributes_are_in_body(request_body)
        validate_no_empty_attributes(request_body)
        validate_task_id(request_body)
        validate_status(request_body)
        #save task to json file
        save_json_task(request_body)
        return api_response(request_body,"Added data")
    except ValueError as ex:
        log_exception(ex) #log errors in file
        return api_response(message= str(ex)), 400
    except Exception as ex:
        log_exception(ex) #log errors in file
        return api_response(message= "Unexpected error"), 500 #unexpected generic error with generic message

#READ
@app.route("/task", methods = ["GET"])
def read_task():
    try:
        filtered_task_list= load_data(task_list_path) #Load data (task_list)
        status_filter = request.args.get("status")
        if status_filter:
            filtered_task_list = list(
                filter(lambda task: task["status"] == status_filter.lower(), filtered_task_list) #lower case for added flexibility for the user
            )
        return api_response(filtered_task_list,"task list")
    except ValueError as ex:
        log_exception(ex) #log errors in file
        return api_response(message= str(ex)), 400
    except Exception as ex:
        log_exception(ex) #log errors in file
        return api_response(message= "Unexpected error"), 500 #unexpected generic error with generic message    

#UPDATE
@app.route("/task/<task_id>", methods = ["PUT"])
def update_task(task_id):
    try:
        request_body = request.json
        #validations
        file_index = find_task_file_index(task_id) #returns error if task_id is not found
        validate_attributes_are_in_body(request_body)
        validate_no_empty_attributes(request_body)
        validate_status(request_body)
        validate_task_id(request_body,task_id) #returns error only if task id is being updated to a value that already exists
        
        update_task_json(file_index,request_body) 
        return api_response(request_body,"Update data")
    except ValueError as ex:
        log_exception(ex) #log errors in file
        return api_response(message= str(ex)), 400
    except Exception as ex:
        log_exception(ex) #log errors in file
        return api_response(message= "Unexpected error"), 500 #unexpected generic error with generic message     

#DELETE
@app.route("/task/<task_id>", methods = ["DELETE"])
def delete_task(task_id):
    try:
        delete_task = delete_task_from_json(task_id)
        return api_response(delete_task,"Deleted data")
    except ValueError as ex:
        log_exception(ex) #log errors in file
        return api_response(message= str(ex)), 400
    except Exception as ex:
        log_exception(ex) #log errors in file
        return api_response(message= "Unexpected error"), 500 #unexpected generic error with generic message 

if __name__ ==   "__main__":
    app.run(host="localhost", debug = True)








