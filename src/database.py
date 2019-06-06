import pymongo


class Database:
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['seismicdb']


    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)


    @staticmethod
    def findOne(collection, query):
        return Database.DATABASE[collection].find(query)

    Database.initialize()
    print( Database.findOne(collection="mapdata",query={"_id" : ObjectId("5bd9d495295a606a9b33f1b5")}))


    db.orders.aggregate([
            { $match: { status: "A" } },
                     { $group: { _id: "$cust_id", total: { $sum: "$amount" } } },
                     { $sort: { total: -1 } }
                   ])
