import os
from flask import Flask, request
app = Flask(__name__)

dbConfigs = { "HOST_IP": os.environ.get("HOST_IP"), "HOST_PORT": os.environ.get("HOST_PORT"), "DB_PORT": os.environ.get("DB_PORT"), "DB_USER": os.environ.get("DB_USER"), "DB_PASS": os.environ.get("DB_PASS") }

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/sample', methods=['GET'])
def sample_post():
    return "param1:{}".format(dbConfigs)