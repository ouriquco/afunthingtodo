from flask import Flask, jsonify,request
from flask_pymongo import PyMongo
app=Flask(__name__)
app.config["MONGO_URI"]="mongodb://localhost:2701/test"

mongo=PyMongo(app)

@app.route('/')

def add_document():
    data=request.json
    if not data:
        return jsonify({"error":"No data provided"}), 400
    
    result=mongo.db.collection.insert_one(data)

    return jsonify({"result": "success", "document_id": str(result.inserted_id)}), 201

def hello():
    return "Welcome to Flask API"

@app.route('/api/data')

def get_data():
    data={'key':'value','numbers':[1,2,3]}
    return jsonify(data)

if __name__=="__main__":
    app.run(debug=True)

@app.route('/api/users/<username>')
def show_user_profile(username):
    return jsonify({'username':username})

@app.route('/api/messages', methods=['GET', 'POST'])
def messages():
    if request.method == 'POST':
        # Code to handle POST request
        return 'Message received!'
    else:
        # Code to handle GET request
        return 'Here are the messages.'
    
if __name__ == '__main__':
    app.run(debug=True)    
