import pymongo
from flask import Flask, request, render_template


app = Flask(__name__)

# mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")  # for run flask by host

mongo_client = pymongo.MongoClient("mongodb://db:27017/")  # for run flask under compose, where mongo service called "db"


def add_to_db(db_name, collection_name, object):

    db = mongo_client[db_name]
    collection = db[collection_name]    
    collection.insert_one(object)


def get_from_db(db_name, collection_name):

    db = mongo_client[db_name]
    collection = db[collection_name]
    all_ = list(collection.find())    
    return all_


@app.route('/')
def hello():
    return render_template("index.html")    


@app.route('/add', methods=['POST', 'GET'])
def add_person():

    if request.method == 'GET':
        return render_template("add.html")            

    new_name = request.form.get("name", "unknown-name")
    add_to_db("db", "users", 
              {'name': new_name})
    
    return render_template("index.html")


@app.route('/all')
def get_people():
    all_records = get_from_db("db", "users")
    names = [x["name"] for x in all_records]
    
    return render_template("all.html", names=names)


app.run(host='0.0.0.0', port=5000, debug=True)
