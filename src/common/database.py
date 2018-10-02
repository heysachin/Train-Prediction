

# Created by Sachin Dev on 01/06/18

import pymongo


class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['train_system']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection, query, data):
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def get_frequency_trains_on_station(collection, train_no):
        # ursor = db.collection.aggregate([{"$match": options}, {"$group": {"_id": groupby, "count": {"$sum": 1}}}])
        # return Database.DATABASE[collection].aggregate([{"$match": {train_no: train_no},{"$group":{train_no}, {"$count": "frequency"}}}])
        pass