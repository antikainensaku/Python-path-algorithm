
INF = float('inf')

# class for edges in adjacency graph
class EdgeNode:
	def __init__(self,nde,wght=0):
		self.node = nde
		self.weight = wght

# class for graph breadth-forst search
class Graph:
	
	def __init__(self,verticeAmount):
		self.numOfVertices = verticeAmount
		self.adjacent_graph = {}
		self.vertices = []
		self.maxH = 0
		
		for x in range(1,int(verticeAmount)+1):
			self.adjacent_graph[x] = []
			self.vertices.append(x)
			
		self.distance = {}
		for x in range(1,int(verticeAmount)+1):
			self.distance[x] = INF
			
		self.pred = {}
		for x in range(1,int(verticeAmount)+1):
			self.pred[x] = None

		
# adds edge (x,y)		
def add_edge(g,x,y,wght):	
	g.adjacent_graph[x].append(EdgeNode(y,wght))
	g.adjacent_graph[y].append(EdgeNode(x,wght))	


def dijkstra(g,s):
	
	for i in g.vertices:
		g.distance[i] = INF
		g.pred[i] = 0
		
	g.distance[s] = 0
	
	queue = [i for i in g.vertices]
	
	while len(queue) > 0:
		minval = INF
		u = 0
		for vert in queue:
			if g.distance[vert] < minval:
				minval = g.distance[vert]
				u = vert
		queue.remove(u)			
		
		for edge in g.adjacent_graph[u]:
			v = edge.node
			if g.distance[v] > max(g.distance[u], edge.weight):
				g.distance[v] = max(g.distance[u], edge.weight)
				g.pred[v] = u
				
		
def print_path(g,u):
	if g.pred[u] != 0:
		print_path(g,g.pred[u])
	print("From:", g.pred[u], "to:", u,)
