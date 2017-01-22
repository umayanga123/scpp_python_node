'''
Tranaction level Test Code
'''

def TransactionVerifyLevelCheck(M,N):

    #print  M ,N , float(M)/N
    tranaction_propability = (float(M)/N) /100;
    verification_lavel = 0.0075;

    #print tranaction_propability

    if(tranaction_propability>=verification_lavel):
        print "Transaction Verified : %s"   %tranaction_propability;
    else:
        print "Transaction Not Verified  :%s"  %tranaction_propability;


TransactionVerifyLevelCheck(75,100);
