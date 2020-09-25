from flask import Flask
from flask import request
import json

app = Flask(__name__)

count1 = 0 
courses = {}

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


@app.route('/ut/courses', methods=['POST'])
def add_course():
    print("Received request.")
    course = request.json
    print("Received data:" + str(course))
    global count1
    count1 = count1 + 1
    courses[count1] = course
    course_with_id = course
    course_with_id['id'] = str(count1)
    return course_with_id


@app.route('/ut/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    print("Received request: " + str(course_id))
    course = courses[course_id] 
    return course

