# Uncertainty_Modelling_in_AI

## This document describes the functions used in sol3.py for CS5340 : Assignment-2 

# edge_pot() -- defines the edge potential between two nodes 
# pot_() -- defines the node potential of individual node
# marginal() -- calculates the marginal of the nodes when called by mutiplying the incoming messages to the self node potential
# send () -- function calculates the outgoing messages to all the neighbours of all the nodes
# receive() -- function calculates the incoming messages from all the neighbours 

# after calling send() and receive() all the nodes have the set of all messages from the whole tree and therefore calculating marginal becomes simpler
