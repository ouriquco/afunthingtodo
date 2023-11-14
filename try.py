import pymongo
from pymongo import MongoClient
import certifi
cluster = MongoClient("mongodb+srv://budrangel:element1@cluster0.smfeewz.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())

def driver():
    try:
        # MongoDB connection URI with SSL options
        
        db = cluster["afunthingtodo"]
        collection = db['user']

        # Data to insert
        singleUser = {"username": "budrangel"}

        # Inserting dat
        collection.insert_one(singleUser)
        print("Data inserted successfully")

    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s" % e)
    except Exception as e:
        print("An error occurred: %s" % e)

if __name__ == '__main__':
    driver()
