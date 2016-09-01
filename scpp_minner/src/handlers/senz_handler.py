import socket
import threading
import tkMessageBox

from db.db_handler import db_handler
from minner_algo_handler.minning_algo import minning_algo
from utils.senz_parser import *
from utils.crypto_utils import *
from config.config import *

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

filehandler = logging.FileHandler('logs/minner.log')
filehandler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
filehandler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(filehandler)


class SenzHandler():
    """
    Handler incoming senz messages from here. We are dealing with following
    senz types
        1. GET
        2. PUT
        3. SHARE
        4. DATA

    According to the senz type different operations need to be carry out
    """

    def __init__(self, transport):
        """
        Initilize udp transport from here. We can use transport to send message
        to udp socket

        Arg
            trnsport - twisted transport instance
        """
        self.transport = transport


    def handleSenz(self, senz):
        """
        Handle differennt types of senz from here. This function will be called
        asynchronously. Whenc senz message receives this function will be
        called by twisted thread(thread safe mode via twisted library)
        """
        print "Hanlder ", senz.attributes, senz.type, senz.receiver, senz.sender

        logger.info('senz received %s' % senz.type)
        dbh = db_handler()

        if (senz.type == 'PUT'):
            print "Coin value :", senz.attributes["#COIN_VALUE"]
            senze = 'UNSHARE #COIN_VALUE '
            senz = str(senze) + "@%s  ^%s" % (senz.sender, clientname)
            signed_senz = sign_senz(senz)
            logger.info('read senz: %s' % signed_senz)
            self.transport.write(signed_senz)

        elif (senz.type == "SHARE"):
            flag = senz.attributes["#f"]
            if (flag == "cc"):
                cah = minning_algo()
                coin = cah.getCoin(senz.attributes["#S_PARA"])

                senze_c = 'PUT #COIN %s ' % coin
                senz_c = str(senze_c) + "@%s  ^%s" % (senz.sender, clientname)
                signed_senzc = sign_senz(senz_c)

                dbh.addMinerDetail(senz.attributes, coin)

                logger.info('Auto Excute: %s' % signed_senzc)
                self.transport.write(signed_senzc)
                self.sendTDetailsToBase(senz)
        elif (senz.type=="UNSHARE"):
            pass

    def postHandle(self, arg):
        """
        After handling senz message this function will be called. Basically
        this is a call back funcion
        """
        #print "post Handelr"
        logger.info("Post Handled")
        return

    def coinValueReguest(self):
        senze = 'SHARE #COIN_VALUE  #f cv @baseNode '
        senz = str(senze) + " ^%s" % (clientname)
        signed_senz = sign_senz(senz)
        logger.info('read senz: %s' % signed_senz)

        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Connect the socket to the port where the server is listening
        server_address = (serverhost, serverport)
        sock.connect(server_address)
        sock.sendto(signed_senz, server_address)
        data = sock.recvfrom(4096)
        x = parse(data[0])

        # print "wada" , x.attributes["#COIN_VALUE"]
        tkMessageBox.showinfo("Message - Coin Rate  ", "Coin Value  :" + x.attributes["#COIN_VALUE"] + "$")
        sock.close()

        thread = threading.Thread(target=self.restartProdocole, args=())
        thread.start()
        return

    def restartProdocole(self):
        import miner

        try:
            miner.start()
        except:
            pass

    def sendTDetailsToBase(self, senz):
        senze_c = 'SHARE #M_S_ID  #f "td" #NO_COIN  #S_ID  '
        senz_c = str(senze_c) + "@%s  ^%s" % ("baseNode", clientname)
        signed_senzc = sign_senz(senz_c)
        self.transport.write(signed_senzc)

        senze_d = 'DATA #M_S_ID %s #f %s #NO_COIN %s #S_ID %s ' % ("M_1", "td","1", senz.attributes["#S_ID"])
        senz_d = str(senze_d) + "@%s  ^%s" % ("baseNode", clientname)
        signed_senzd = sign_senz(senz_d)
        self.transport.write(signed_senzd)

        senze_u = 'UNSHARE #M_S_ID  #f #NO_COIN  #S_ID  '
        senz_u = str(senze_u) + "@%s  ^%s" % ("mysensors", clientname)
        signed_senzu = sign_senz(senz_u)
        self.transport.write(signed_senzu)


