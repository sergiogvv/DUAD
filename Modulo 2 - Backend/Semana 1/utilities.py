from json import (load as jsonload, dump as jsondump, loads as jsonloads, dumps as jsondumps)
from os import path
from persistance import load_data, save_data

status_list = ["pending", "in progress","complete"]

task_list_path= path.join(path.dirname(__file__), r'task_list.json')
task_list= load_data(task_list_path)

def validate_attributes_are_in_body(request_body):
    if "id" not in request_body:
        raise ValueError("task id missing from the body")
    if "title" not in request_body:
        raise ValueError("title missing from the body")
    if "description" not in request_body:
        raise ValueError("description missing from the body")
    if "status" not in request_body:
        raise ValueError("status missing from the body")
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


def validate_task_id(request_body):
    for task in task_list:
        if request_body["id"] == task["id"]:
            raise ValueError("id already exists")
    return True


def save_json_task(request_body): #save task to json file
    task_list.append(request_body)
    json_tasks = jsondumps(task_list, indent=2)
    save_data(json_tasks, task_list_path)


def update_task_json(task_id,request_body):
    for i in range(0,len(task_list)):
        if str(task_list[i]["id"]) == task_id:
            task_list[i] = request_body
            json_tasks = jsondumps(task_list, indent=2)
            save_data(json_tasks, task_list_path)
            return True
    raise ValueError('Task not found')


def delete_task_from_json(task_id): #delete task from json file
    for i in range(0,len(task_list)):
        if str(task_list[i]["id"]) == task_id:
            delete_task = task_list.pop(i)
            json_tasks = jsondumps(task_list, indent=2)
            save_data(json_tasks, task_list_path)
            return delete_task
    raise ValueError('Task not found')





def find_task_id(task_id):
        for task in task_list:
            if task_id == task["id"]:
                return True
        return False


def validate_status(request_body):
    if request_body["status"] not in status_list:
        raise ValueError("status not valid")
    return True
