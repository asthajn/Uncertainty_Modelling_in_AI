from numpy import array, matrix, prod, sum, ones

def edge_pot(i,j):       #d efines the edge potential 
	if i==j:
		return 1.0
	else:
		return 0.5

def pot_(x): # defines the node potential for each node as given in the question
	if(x%2 ==0):
		return array([0.7,0.3])
	else:
		return array([0.1,0.9])

class Node():
	
	def __init__(self,edge_pot):
		self.edge_pot=edge_pot
	edge_pot = []
	nbrs = [] #list of neighbours - int
	incoming = [] # list of incoming messages from neighbours
	outgoing = [] # list of outgoing to neighbours

	def marginal(self):
		p = prod(self.incoming.values(),0)
		p = self.edge_pot*p
		return p/(sum(p))

class calV():
	V = [(Node(pot_(x))) for x in range(6)]
	V[0].nbrs = [1,2]
	V[1].nbrs = [0,3,4]
	V[2].nbrs = [0,5]
	V[3].nbrs = [1]
	V[4].nbrs = [1]
	V[5].nbrs = [2]

	for i in range(6):
		for j in V[i].nbrs:
			V[i].outgoing = dict([(x,array([1,1])) for x in V[i].nbrs])
			V[i].incoming = dict([(x,array([1,1])) for x in V[i].nbrs])

	def send(self):
		for i in range(6):
			for j in self.V[i].nbrs:
				self.V[i].outgoing[j] = array([0,0])
				for in_ in range(2):
					self.V[i].outgoing[j] = (self.V[i].outgoing[j] + self.V[i].edge_pot[in_]*array([edge_pot(in_,0) , edge_pot(in_,1)]) \
						* prod([self.V[i].incoming[x][in_] for x in self.V[i].nbrs if x!=j]))

	def receive(self):
		for i in range(6):
			for j in self.V[i].nbrs:
				self.V[i].incoming[j] = self.V[j].outgoing[i]

def main():
	a = calV()
	for k in range(6):
		a.send()
		a.receive()

	for k in range(6):
		print "Marginal for node number ",k+1,"is",a.V[k].marginal()

if __name__ == '__main__':
	main()

