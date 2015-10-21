# Uncertainty_Modelling_in_AI

## This document describes the functions used in sol3.py for CS5340 : Assignment-2 

# edge_pot() -- defines the edge potential between two nodes 
# pot_() -- defines the node potential of individual node
# marginal() -- calculates the marginal of the nodes when called by mutiplying the incoming messages to the self node potential
# send () -- function calculates the outgoing messages to all the neighbours of all the nodes
# receive() -- function calculates the incoming messages from all the neighbours 

# after calling send() and receive() all the nodes have the set of all messages from the whole tree and therefore calculating marginal becomes simpler

SOLUTION :

Marginal for node number  1 is [ 0.59098405  0.40901595]
Marginal for node number  2 is [ 0.10161794  0.89838206]
Marginal for node number  3 is [ 0.59622558  0.40377442]
Marginal for node number  4 is [ 0.06575926  0.93424074]
Marginal for node number  5 is [ 0.56742955  0.43257045]
Marginal for node number  6 is [ 0.12965594  0.87034406]

