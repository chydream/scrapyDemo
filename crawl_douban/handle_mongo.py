import pymongo

class Handle_Mongo(object):
    def __init__(self):
        myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
        myclient.admin.authenticate("admin", "123456")
        mydb = myclient['douban']
        self.mycollection = mydb['douban_data']

    def handle_save_data(self, item):
        self.mycollection.insert_one(item)

douban_mongo = Handle_Mongo()