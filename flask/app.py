from flask import Flask, request
import pymongo

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
    return "<h1> Welcome to flask + mongo app. </h1> <p> try goto: <br/>http://localhost:5000/add?name=david </p> "


@app.route('/add')
def add_person():
    query_params = request.args.to_dict()

    add_to_db("my_db", "my_collection", 
              {'name': query_params.get("name", "unknown")})
    
    return """<h1> Added </h1>
    <a href="http://127.0.0.1:5000/get"> show all </a> """

@app.route('/get')
def get_people():
    all_records = get_from_db("my_db", "my_collection")
    res = "<h1> all records: </h1> <p>"
    res += str([rec['name'] for rec in all_records])
    res += "</p> <a href='http://127.0.0.1:5000'> home </a>"
    return res


app.run(host='0.0.0.0', port=5000)
