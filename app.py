import os
from flask import Flask, render_template, url_for, request, redirect
from pymongo import MongoClient
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

client = MongoClient('localhost', 27017)

@app.route("/", methods=['GET', 'POST'])
def index():      
    return render_template('index.html')

db = client.flask_database
tasks = db.tasks


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=os.environ.get("PORT"),
    debug=True)
    
    