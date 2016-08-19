from pymongo import MongoClient
import datetime

class db_handler:

   global collection;
   global db;

   def __init__(self):
       client = MongoClient('localhost', 27017)
       self.db = client.scpp_stock_exchange

   def addTransaction(self,quarry):
       #print quarry["#M_S_ID"]
       self.collection = self.db.transaction_detail
       transaction ={"M_S_ID": quarry["#M_S_ID"], "NO_COIN": int(quarry["#NO_COIN"]), "S_ID":int(quarry["#S_ID"]),"date": datetime.datetime.utcnow()}
       self.collection.insert(transaction)
       return 'DONE'


   def testData(self):
       self.t_collection =self.db.transaction_detail
       self.m_collection =self.db.service_detail

       if (self.m_collection.count() == 0):
           services = [{"S_ID":1, "COIN_VALUE":50}
            ,{"S_ID":2, "COIN_VALUE":45}
           ,{"S_ID":3, "COIN_VALUE":30}
           ,{"S_ID":4, "COIN_VALUE":10}]

           transaction = {"M_S_ID": 2, "NO_COIN":3, "S_ID": 4,"date": datetime.datetime.utcnow()}

           self.m_collection.insert_many(services)
           self.t_collection.insert(transaction)
           print "create test service_detail  transaction table"



