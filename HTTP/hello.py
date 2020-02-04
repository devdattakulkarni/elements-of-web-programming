from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/web-programming/')
def hello_web_programming():
    return 'Hello, Web Programming!'


@app.route('/queryparam')
def queryparam():
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')
    return 'Param1: ' + param1 + ' Param2: ' + param2

