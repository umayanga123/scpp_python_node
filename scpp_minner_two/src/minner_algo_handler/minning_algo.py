import hashlib


class minning_algo:


    def __init__(self):
        #print "call mining algo class"
        pass



    def getCoin(self,arg):
        coin = hashlib.sha1(arg.encode("UTF-8")).hexdigest()
        ##return coin[:20]
        return coin