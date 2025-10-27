from json import (load as jsonload, dump as jsondump, loads as jsonloads, dumps as jsondumps)
from os import path
from datetime import datetime, timezone
from flask import Flask, request, jsonify
from json import (load as jsonload, dump as jsondump, loads as jsonloads, dumps as jsondumps)



def api_response(data=None, message=""):
    return jsonify({
        "message": message,
        "data": data,
    })

def check_user_attributes(request_body):
    allowed_keys = ("full_name", "email", "username", "password", "DOB", "account_status")
    for key in request_body.keys():
        if key not in allowed_keys:
            raise ValueError(f"Unexpected key in body: {key}")
    return True