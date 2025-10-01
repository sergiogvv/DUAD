from flask import Flask, request, jsonify
from os import path
from persistence import load_data, save_data
import products

app = Flask(__name__)



















if __name__ ==   "__main__":
    app.run(host="localhost", debug = True)