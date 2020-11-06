import json

from flask import request
from flask import Flask, render_template


application = Flask(__name__)
app = application
all_pools = []

@app.route("/static/search_libraries", methods=['POST'])
def get_libraries():

    # Assignment 4: Insert Pool into database.
    # Extract all the form fields
    pool_name = request.form['pool_name']
    status = request.form['status']
    print("Pool Name:" + pool_name)
    print("Status:" + status)

    # Insert into database.


    return render_template('pool_added.html')


@app.route("/pools")
def get_pools():
    # Assignment 4: 
    # Query the database to pull all the pools
    # Sample pool -- Delete this from final output.
    pool = {}
    pool['Name'] = 'Barton Springs'
    pool['Timings'] = 'Friday - Sunday'
    pool['Status'] = 'Open'
    all_pools.append(pool)
    return json.dumps(all_pools)


@app.route("/")
def pool_info_website():
    return render_template('index.html')


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
