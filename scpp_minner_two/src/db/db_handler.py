import datetime

from pymongo import MongoClient


class db_handler:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client.scpp_miner_two
        self.collection = self.db.miner_detail

    def addMinerDetail(self, quarry, coin, formatedate):

        print quarry
        miner_object = {"M_S_ID": "M_2", "S_ID": int(quarry["#S_ID"]), "S_PARA": quarry["#S_PARA"],"COIN": str(coin), "NO_COIN": int(1), "date": formatedate}
        print miner_object
        self.collection.insert(miner_object)
        return 'ADD DATA SUCCESSFULLY'

    '''
    return all miner_detail table data
   '''

    def getAllMinerDetails(self):
        md = self.db.miner_detail.find()
        return md
