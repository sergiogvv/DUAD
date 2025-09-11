from flask import Flask, request
app = Flask(__name__)

def validate_attributes(task_id,title,description,status):
    try:
        if task_id.strip() == "":
            raise ValueError
        if title.strip() == "":
            raise ValueError
        if description.strip() == "":
            raise ValueError
        if status.strip() == "":
            raise ValueError
    except:
        pass


def validate_task_id():
    for i in range(0,len(task_list)):
        pass




status_list = ["pending", "in progress","complete"]

task_list = [
    {
        "task_id": 12345,
        "title": "full disk scan",
        "description": "scan every disk sector",
        "status": "pending"
    }
]

#CREATE
@app.route("/create_task", methods = ["POST"])
def create_task():
    request_body = request.json

    return request_body

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
def delete_task():
    pass

@app.route("/")
def root():
    print("Hola mundo!!!!!!")
    return "<h1>Hello World!!!!!</h1>"

@app.route("/information", methods=["GET","POST"])
def information():
	return {
		"year": 2024,
		"description": "Esto es un endpoint secundario",
	}

@app.route("/echo", methods=["POST"])
def echo():
    request_body = request.json
    return request_body

if __name__ ==   "__main__":
    app.run(host="localhost", debug = True)








