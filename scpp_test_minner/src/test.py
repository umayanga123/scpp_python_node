import hashlib
import datetime
from pyblake2 import blake2b

key = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(n, plaintext):
    """Encrypt the string and return the ciphertext"""
    result = ''

    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.lower()


def decrypt(n, ciphertext):
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result


def show_result(plaintext, n):
    """Generate a resulting cipher with elements shown"""
    print "TEST ALGO"
    encrypted = encrypt(n, plaintext)
    decrypted = decrypt(n, encrypted)

    print 'Rotation: %s' % n
    print 'Plaintext: %s' % plaintext
    print 'Encrytped: %s' % encrypted
    print 'Decrytped: %s' % decrypted

    m = hashlib.md5()
    m.update(encrypted)
    print  '\n'
    print m.hexdigest()
    return m;


def getCoin(arg):
    coin = hashlib.sha256(arg.encode("UTF-8")).hexdigest()
    ##return coin[:20]
    return coin


#show_result('the grass is always greener', 115)

#MINER OR APP SECRECT (CECER CYPER OUT PUT HASHES USING MD5-128bit(16 hex)  )
secrect_text ="the grass is always greener"
secrect_no = 30
secrect_value = encrypt(secrect_no,secrect_text);

#COIN GENRATE DATE
format_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace(" ", "")

#TAKE GIVEN OTHIER PARAMETERS AND GENERATE COIN ID. + paramete rsting concatanation md5 value
coin = getCoin("500km"+""+format_date+""+"M1"+secrect_text)
print "Coin_ID :" , coin;

#reducse size to coin name sting
coin_name = blake2b(digest_size=10)
coin_name.update(coin)
#coin_name.hexdigest()
print "coin name :" , coin_name.hexdigest() + ".scpp"

f= open(coin_name.hexdigest()+ ".scpp","w+")
f.write("ID :%s\r\n" % coin)


curdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print "Request TIME :", curdate;
f.write("TIME :%s\n" % curdate+"")

sender = raw_input("Enter Sender Public key :");
print sender;
f.write("IN  :%s\n" % sender)

receiver = raw_input("Enter Receiver key  :");
print receiver;
f.write("OUT :%s\n" % receiver)



f.write("AMOUNT :%d\r\n" % 1)
print "Add coin amount(Default 1)"
f.write("Signature :%s\r\n" % "asdemdeofrffgrmdfldesdderfvspwertw")
print "Add Sender Digital Signature\n"
print "coin \n"

f.close()



f=open(coin_name.hexdigest()+ ".scpp", "r")
contents =f.read()
print contents