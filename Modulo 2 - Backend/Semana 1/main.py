from flask import Flask, request, jsonify
app = Flask(__name__)

def validate_attributes_are_in_body(request_body):
    try:
        if "id" not in request_body:
            raise ValueError("task id missing from the body")
        if "title" not in request_body:
            raise ValueError("title missing from the body")
        if "description" not in request_body:
            raise ValueError("description missing from the body")
        if "status" not in request_body:
            raise ValueError("status missing from the body")
        return True
    except ValueError as ex:
        return ex


def validate_no_empty_attributes(request_body):
    try:
        if str(request_body["id"]).strip() == "":
            raise ValueError("task id can not be empty")
        if str(request_body["title"]).strip() == "":
            raise ValueError("title can not be empty")
        if str(request_body["description"]).strip() == "":
            raise ValueError("description can not be empty")
        if str(request_body["status"]).strip() == "":
            raise ValueError("status can not be empty")
        return True
    except ValueError as ex:
        return ex


def validate_task_id(request_body):
    try:
        for task in task_list:
            if request_body["id"] == task["id"]:
                raise ValueError("id already exists")
        return True
    except ValueError as ex:
        return ex


def find_task_id(task_id):
        for task in task_list:
            if task_id == task["id"]:
                return True
        return False


def validate_status(request_body):
    try:
        if request_body["status"] not in status_list:
            raise ValueError("status not valid")
        return True
    except ValueError as ex:
        return ex


status_list = ["pending", "in progress","complete"]

task_list = [
    {
        "id": 12345,
        "title": "full disk scan",
        "description": "scan every disk sector",
        "status": "pending"
    }
]

#CREATE
@app.route("/create_task", methods = ["POST"])
def create_task():
    request_body = request.json
    attributes_present = validate_attributes_are_in_body(request_body)
    if attributes_present == True:
        no_empty_attributes = validate_no_empty_attributes(request_body)
        if no_empty_attributes == True:
            valid_id = validate_task_id(request_body)
            if valid_id == True:
                valid_status = validate_status(request_body)
                if valid_status == True:
                    task_list.append(request_body)
                    return jsonify(data=task_list), 200
                else:
                    return jsonify(message=str(valid_status)), 400
            else:
                return jsonify(message=str(valid_id)), 400
        else:
            return jsonify(message=str(no_empty_attributes)), 400    
    else:
        return jsonify(message=str(attributes_present)), 400

#READ
@app.route("/read_tasks")
def read_task():
    filtered_task_list = task_list
    status_filter = request.args.get("status")
    if status_filter:
        filtered_task_list = list(
            filter(lambda task: task["status"] == status_filter, filtered_task_list)
        )
    return {"task list": filtered_task_list}

#UPDATE
@app.route("/update/<task_id>", methods = ["PUT", "PATCH"])
def update_task():
    if request.method == "PUT":
        pass
    else:
        pass

#DELETE
@app.route("/delete/<task_id>", methods = ["DELETE"])
def delete_task(task_id):
    for i in range(0,len(task_list)):
        if str(task_list[i]["id"]) == task_id:
            delete_task = task_list.pop(i)
            return jsonify(deleted=delete_task), 200
    return jsonify(message='Task not found'), 400     


if __name__ ==   "__main__":
    app.run(host="localhost", debug = True)








