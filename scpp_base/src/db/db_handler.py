import datetime

from pymongo import MongoClient

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

   #test function , if it database is empty put data to db.
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
           print 'create test service_detail  transaction table'
           return 'done'



   def calulateCoinsValue(self):

       totalcoin =0;
       generate_coin_value=0;

       self.t_collection = self.db.transaction_detail
       self.m_collection = self.db.service_detail


       #This method take all number of generate new crypto coin

       cursor = self.t_collection.aggregate(
           [
               {"$group": {"_id":"", "total_coin": {"$sum": "$NO_COIN"}}}
           ]

       )

       #This method join two table and return that new table
       cursor1= self.t_collection.aggregate([
            { "$lookup":
                {
                    'from': "service_detail",'localField': "S_ID","foreignField": "S_ID",'as': "coin_detail"

                }
            }
       ])


       #assign total generate new coin numebr
       for document in cursor:
           totalcoin = document['total_coin']


       #calculate value of coins
       for document in cursor1:
           generate_coin_value += document['NO_COIN'] * document['coin_detail'][0]['COIN_VALUE']

       #calculate cripto coin value
       if(totalcoin != 0):
           self.cv= (generate_coin_value / totalcoin) * 0.01
       else:
           self.cv = 0

       return self.cv


   #this methoth shout be implment take coin value with out excute calculator function
   def getCoinValue(self):
       #not yet implement
       return 000;


   '''
    retunr all service detals table data
   '''
   def getAllServiceDetail(self):
       self.m_collection = self.db.service_detail
       return self.m_collection

   '''
    return all transaction table data
   '''
   def getAllTransactionDetails(self):
       self.t_collection = self.db.transaction_detail.find()
       return self.t_collection