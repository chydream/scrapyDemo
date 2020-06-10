from pymongo import MongoClient

# client = MongoClient(host="localhost", port=27017)
# client.admin.authenticate("admin", "123456")
myclient = MongoClient("mongodb://127.0.0.1:27017")
myclient.admin.authenticate("admin", "123456")
mydb = myclient['imooc']
mycollection = mydb['pymongo_test']
mycollection.insert_one({"name": "imooc", "flag": 1, "url": "http://www.baidu.com"})

# result = mycollection.find({}, {'_id': 0, "name": 1, "flag": 1})
# result = mycollection.find({"name": {"$regex": "^G"}})
mycollection.delete_many({"url": {"$regex": "https?://www.\.[tq]"}})