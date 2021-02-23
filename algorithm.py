# Python code to perform Dijkstra's algorithm
# in a non-directed graph

INF = float('inf')

# We assume that nodes numbered from 1 to n

# class for edges in adjacency list
class WeightedEdgeNode:
	def __init__(self,nde,wght=0):
		self.node = nde
		self.weight = wght

# graph class for breadth-forst search 
class WeightedGraph:
	
	def __init__(self,nVerts):
		self.nVertices = nVerts
		self.adj_list = {}
		self.vertices = []
		
		for x in range(1,int(nVerts)+1):
			self.adj_list[x] = []
			self.vertices.append(x)
			
		self.dist = {}
		for x in range(1,int(nVerts)+1):
			self.dist[x] = INF
			
		self.pred = {}
		for x in range(1,int(nVerts)+1):
			self.pred[x] = None

		
# adds edge (x,y)		
def add_edge(g,x,y,wght):	
	g.adj_list[x].append(WeightedEdgeNode(y,wght))
	g.adj_list[y].append(WeightedEdgeNode(x,wght))	


def dijkstra(g,s):
	
	for i in g.vertices:
		g.dist[i] = INF
		g.pred[i] = 0
		
	g.dist[s] = 0
	
	queue = [i for i in g.vertices]
	
	while len(queue) > 0:
		minval = INF
		u = 0
		for vert in queue:
			if g.dist[vert] < minval:
				minval = g.dist[vert]
				u = vert
		queue.remove(u)			
		
		for edge in g.adj_list[u]:
			v = edge.node
			#DEBUGG
			#print("g.dist[v]: {} g.dist[u]: {} edge.weight: {}".format(g.dist[v], g.dist[u], edge.weight))
			if g.dist[v] > g.dist[u] + edge.weight:
				g.dist[v] = g.dist[u] + edge.weight
				g.pred[v] = u
				
		#DEBUG INFO:
		#print(u, " processed, dist =  ",g.dist[u])
		
def print_path(g,u):
	if g.pred[u] != 0:
		print_path(g,g.pred[u])
	print(u,':',g.dist[u])
