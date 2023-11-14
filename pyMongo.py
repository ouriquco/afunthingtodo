import pymongo
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://<budrangel>:<JoeBiden2023>@cluster0.smfeewz.mongodb.net/?retryWrites=true&w=majority")
db= cluster["afunthingtodo"]

def driver():
    collection=db['user']
    singleUser={"username":"budrangel"}
    collection.insert_one(singleUser)

if __name__ == '__main__':
    driver()