# scpp_python_node
##Protocols:-
####SHARE #pubkey PEM_PUBKEY @receiver #time timeOfRequest ^sender signatureOfTheSenze

Used to share key/data with other components where this protocol consists of public key, receiver node name and time of request. SHARE protocol can be used with or without data.
####PUT #COIN_VALUE {parm} @receiver #time timeOfRequest ^sender signatureOfTheSenze

PUT protocol can be used when one client want to add some value to data shared by another client. For that received message, time and prior data shared client's name must be passed in the protocol.
####UNSHARE #COIN_VALUE @receiver #time timeOfRequest ^sender signatureOfTheSenze

UNSHARE protocol is the inverse of share protocol where client used to unshare keys with components with the format of key, receiver node name and time.
####DATA #f "td" #M_S_ID <parm> #NO_COIN <parm> #S_ID <parm> @receiver #time timeOfRequest ^sender signatureOfTheSenze

Used when client wants to add value to a data shared by him/herself before. DATA protocol format consists of message, time and receiver node name. 

##Currency Mining Component (Minner/ Test_Miner):-


Mining component is a majority Python based currency miner for coin generation. The following
development milestones had been achieved in it so far:

 Implementation of a currency miner's communication node through two Python clients


 Designed the basic coin structure: by using a primary level of Mining Algorithm where it generates a hash value as a coin by integrating service id, service type etc sort of data at this stage


 Implementation of the Coin Generation module


 o Achieved mined coin details tracking
 
 o Generation of coin value automate
 
 Designed and development of component level non-relational databases (Miner , Base ) 

 Completion of API and protocol based connections between
o Base Node – Coin Generation Module
o Switch – Coin Generation Module


 Python Asynchronous exception handling in miner and base module


 Achieving the level of unit testing and completion of Testing and Code Refactoring of the current
developments

####With the following functions that can be performed through this component with the completion of above mentioned milestones contribute to the overall system.

 Generate coins for the incoming service requests: Only a single coin per service get generated
currently

 Store the data of incoming service requests as microservices architecture using MongoDB

 Send the most required limited data among those stored details to Base

##Service Component (Base & Switch)

Service component is in responsible for performing communications between nodes and handling currency transactions. The development progress of it so far is as follows:

 Initialized database connections of the routing database and Android databases for the
developed Python clients

 Design and Development of Base Node

 Finalized Switch development

 Initialized basic secure verification mechanism in transactions

 Completion of API and protocol based connections between
o Switch – Base Node
o Switch – Android Client Apps

 Code Refactoring of the current developments and achieving the level of unit testing and
completion of Testing

####With the completion of above milestones the contribution it supplies for overall system at this stage can be listed as below.

 Store details about generated coins such as service id

 Process coin details and determine a primary value for a coin: coin values are hard corded at this
stage

 Send a determined coin value to other requesting modules 

##Application Component

Application component is about currency storing at client side with a digital wallet and user management.Up to this stage the following milestones has been achieved in development perspective.

 Development of protocol connection between Coin Generation Module and Android apps

 Achieving the level of unit testing and completion of Testing and Code Refactoring of the current
developments

####This offers the following functionalities currently to the overall system as results of the above milestones completion.

 Provide coin based services such as carpooling, buying items from shops

 Send coin mining requests to Mining component for the offered services

 Retrieve coins from miner and store coins in wallet

 Provide coins to be transferred between registered users as Peer-to-Peer transactions: coins are transferred as it is without any splitting at this stage
