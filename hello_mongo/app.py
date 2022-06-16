import pymongo

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = mongo_client["mapsa"]
mycol = mydb["django"]

mydict = { "name": "Majedi", "address": {"1": "tehran", "2": "kermanshah", "3": "tabriz"}, "age": 32}

x = mycol.insert_one(mydict)