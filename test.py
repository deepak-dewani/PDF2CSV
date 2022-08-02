import pymongo
from pymongo import MongoClient

cluster = MongoClient("localhost:27017")
db = cluster["test_connection"]
collection = db["test"]

post = {"name": "deepak", "score": 96}
post1 = {"_id": 1, "name": "rishabh", "score": 97}
post2 = {"_id":2, "name": "tim", "score":50}
post3 = {"_id":3, "name": "john", "score":66}

collection.insert_many([post1, post2])