from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.todo_db
collection = db.todo_items

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    data = request.get_json()
    itemName = data.get("itemName")
    itemDescription = data.get("itemDescription")

    if not itemName or not itemDescription:
        return jsonify({"message": "Both fields are required"}), 400

    # Store in MongoDB
    collection.insert_one({
        "itemName": itemName,
        "itemDescription": itemDescription
    })

    return jsonify({"message": "To-Do item saved successfully!"})
