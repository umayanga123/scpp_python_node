import datetime

from pymongo import MongoClient


class db_handler:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client.scpp_miner
        self.collection = self.db.miner_detail

    def addMinerDetail(self, quarry, coin, formatedate):

        print quarry
        miner_object = {"M_S_ID": "M_1", "S_ID": int(quarry["#S_ID"]), "S_PARA": quarry["#S_PARA"],"COIN": str(coin), "NO_COIN": int(1), "date": formatedate}
        print miner_object
        self.collection.insert(miner_object)
        return 'ADD DATA SUCCESSFULLY'

    '''
    return all miner_detail table data
   '''

    def getAllMinerDetails(self):
        md = self.db.miner_detail.find()
        return md

    def getAllBlockChainDetail(self):
        bc = self.db.block_chain.find()
        return bc

    # added new method  create block chain_structure
    def addCoinWiseTransaction(self, senz, coin, format_date):
        self.collection = self.db.block_chain
        coinValexists = self.collection.find({"_id": str(coin)}).count()
        print('coin exists : ', coinValexists)
        if (coinValexists > 0):
            print('coin hash exists')
            newTransaction = {"$push": {"TRANSACTION": {"SENDER": senz.attributes["#SENDER"],
                                                        "RECIVER": senz.attributes["#RECIVER"],
                                                        "T_NO_COIN": int(1),
                                                        "DATE": datetime.datetime.utcnow()
                                                        }}}
            self.collection.update({"_id": str(coin)}, newTransaction)
        else:
            flag = senz.attributes["#f"];
            print flag
            if (flag == "ccb"):
                print('new coin mined othir minner')
                root = {"_id": str(coin)
                    , "S_ID": int(senz.attributes["#S_ID"]), "S_PARA": senz.attributes["#S_PARA"],
                        "FORMAT_DATE": format_date,
                        "NO_COIN": int(1),
                        "TRANSACTION": [{"MINER": senz.attributes["#M_S_ID"],
                                         "RECIVER": senz.attributes["#RECIVER"],
                                         "T_NO_COIN": int(1),
                                         "DATE": datetime.datetime.utcnow()
                                         }
                                        ]
                        }
                self.collection.insert(root)
            else:
                print('new coin mined')
                root = {"_id": str(coin)
                    , "S_ID": int(senz.attributes["#S_ID"]), "S_PARA": senz.attributes["#S_PARA"],
                        "FORMAT_DATE": format_date,
                        "NO_COIN": int(1),
                        "TRANSACTION": [{"MINER": "M_1",
                                         "RECIVER": senz.sender,
                                         "T_NO_COIN": int(1),
                                         "DATE": datetime.datetime.utcnow()
                                         }
                                        ]
                        }
                self.collection.insert(root)

        return 'DONE'


