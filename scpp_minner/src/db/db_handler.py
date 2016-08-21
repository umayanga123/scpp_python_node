import datetime

from pymongo import MongoClient


class db_handler:
    global collection;
    global db;

    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client.scpp_miner

    def addTransaction(self, quarry):
        # print quarry["#M_S_ID"]
        self.collection = self.db.transaction_detail
        transaction = {"M_S_ID": quarry["#M_S_ID"], "NO_COIN": int(quarry["#NO_COIN"]), "S_ID": int(quarry["#S_ID"]),"date": datetime.datetime.utcnow()}
        self.collection.insert(transaction)
        return 'DONE'

    '''
    return all transaction table data
   '''

    def getAllTransactionDetails(self):
        self.t_collection = self.db.transaction_detail.find()
        return self.t_collection
