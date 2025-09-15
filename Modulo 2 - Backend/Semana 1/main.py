from flask import Flask, request, jsonify
from os import path
from json import (load as jsonload, dump as jsondump, dumps as jsondumps)

from utilities import validate_attributes_are_in_body, validate_no_empty_attributes, validate_task_id, save_json_task, validate_status, task_list, delete_task_from_json, update_task_json

app = Flask(__name__)



#CREATE
@app.route("/task", methods = ["POST"])
def create_task():
    try:
        request_body = request.json
        #validations
        validate_attributes_are_in_body(request_body)
        validate_no_empty_attributes(request_body)
        validate_task_id(request_body)
        validate_status(request_body)
        #save task to json file
        save_json_task(request_body)

        return {"added data":request_body}
    except ValueError as ex:
        return  jsonify(message=str(ex)), 400
    except Exception as ex:
		# unexpected generic error
        return jsonify(message=str(ex)), 500

#READ
@app.route("/task", methods = ["GET"])
def read_task():
    try:
        filtered_task_list = task_list #imported auxiliary variable from utilities module
        status_filter = request.args.get("status")
        if status_filter:
            filtered_task_list = list(
                filter(lambda task: task["status"] == status_filter, filtered_task_list)
            )
        return {"task list": filtered_task_list}
    except ValueError as ex:
        return  jsonify(message=str(ex)), 400
    except Exception as ex:
		# unexpected generic error
        return jsonify(message=str(ex)), 500    

#UPDATE
@app.route("/task/<task_id>", methods = ["PUT"])
def update_task(task_id):
    try:
        request_body = request.json
        #validations
        validate_attributes_are_in_body(request_body)
        validate_no_empty_attributes(request_body)
        validate_status(request_body)

        update_task_json(task_id,request_body)

        return {"update data":request_body}
    except ValueError as ex:
        return jsonify(message=str(ex)), 400
    except Exception as ex:
		# unexpected generic error
        return jsonify(message=str(ex)), 500     

#DELETE
@app.route("/task/<task_id>", methods = ["DELETE"])
def delete_task(task_id):
    try:
        delete_task = delete_task_from_json(task_id)
        return jsonify(deleted=delete_task), 200
    except ValueError as ex:
        return jsonify(message=str(ex)), 400
    except Exception as ex:
		# unexpected generic error
        return jsonify(message=str(ex)), 500 

if __name__ ==   "__main__":
    app.run(host="localhost", debug = True)








