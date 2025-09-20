from flask import Flask, request, jsonify
from json import (load as jsonload, dump as jsondump, loads as jsonloads, dumps as jsondumps)
from os import path
from persistence import load_data, save_data
from datetime import datetime, timezone

status_list = ["pending", "in progress","complete"]
task_list_path= path.join(path.dirname(__file__), r'task_list.json')
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
        raise ValueError("task id can not be empty")
    if str(request_body["title"]).strip() == "":
        raise ValueError("title can not be empty")
    if str(request_body["description"]).strip() == "":
        raise ValueError("description can not be empty")
    if str(request_body["status"]).strip() == "":
        raise ValueError("status can not be empty")
    return True


def validate_task_id(request_body,task_id=None): # comprehensive id validation, can be used for POST or PUT
    task_list= load_data(task_list_path)
    for task in task_list:
        if request_body["id"] == task["id"]:
            if task_id == None:
                raise ValueError("id already exists")
            if task_id != str(request_body["id"]):
                print(task_id)
                print(request_body["id"])
                raise ValueError("id within request body already exists, please fill in request body id with a different value")
    return True


def save_json_task(request_body): #save task to json file
    task_list= load_data(task_list_path)
    task_list.append(request_body)
    json_tasks = jsondumps(task_list, indent=2)
    save_data(json_tasks, task_list_path)


def find_task_file_index(task_id): # used for PUT (pending test for PATCH) to find index for file to be updated
    task_list= load_data(task_list_path)
    for i in range(0,len(task_list)):
        if str(task_list[i]["id"]) == task_id:
            return i
    raise ValueError('Task not found')

def update_task_json(file_index,request_body):
    task_list= load_data(task_list_path)
    task_list[file_index] = request_body
    json_tasks = jsondumps(task_list, indent=2)
    save_data(json_tasks, task_list_path)


def delete_task_from_json(task_id): #delete task from json file
    task_list= load_data(task_list_path)
    for i in range(0,len(task_list)):
        if str(task_list[i]["id"]) == task_id:
            delete_task = task_list.pop(i)
            json_tasks = jsondumps(task_list, indent=2)
            save_data(json_tasks, task_list_path)
            return delete_task
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
