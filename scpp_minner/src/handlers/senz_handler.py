import sys
import socket
import threading
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
        print self.transport

    def handleSenz(self, senz):
        """
        Handle differennt types of senz from here. This function will be called
        asynchronously. Whenc senz message receives this function will be
        called by twisted thread(thread safe mode via twisted library)
        """

        print  "hnadle call ", senz
        logger.info('senz received %s' % senz.type)

        if(senz.type == 'PUT'):
            print "Coin value :", senz.attributes["#COIN_VALUE"]
            senze = 'UNSHARE #COIN_VALUE '
            senz = str(senze) + "@%s  ^%s" % (senz.sender, clientname)
            signed_senz = sign_senz(senz)
            logger.info('read senz: %s' % signed_senz)
            self.transport.write(signed_senz)

    def postHandle(self, arg):
        """
        After handling senz message this function will be called. Basically
        this is a call back funcion
        """
        print "post Handelr"
        logger.info("Post Handled")
        return

    def coinValueReguest(self):
        senze = 'SHARE #COIN_VALUE @baseNode '
        senz = str(senze) + " ^%s" % (clientname)
        signed_senz = sign_senz(senz)
        logger.info('read senz: %s' % signed_senz)

        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Connect the socket to the port where the server is listening
        server_address = ('127.0.0.1', 9090)
        print >> sys.stderr, 'connecting to %s port %s' % server_address
        sock.connect(server_address)

        print >> sys.stderr, 'sending "%s"' % signed_senz
        sock.sendto(signed_senz, server_address)


        # Receive response
        print >> sys.stderr, 'waiting to receive'
        data, server = sock.recvfrom(4096)
        print data

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
