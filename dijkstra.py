'''
By Saku Antikainen
Student number: 2636168
Idea taken from TRA 2020 example programs

'''

INF = float('inf')

#class for edges in adjacency graph
class EdgeNode:
	def __init__(self,nde,wght=0):
		self.node = nde
		self.weight = wght

#class for graph
class Graph:
	
	def __init__(self,verticeAmount):
		self.numOfVertices = verticeAmount
		self.adjacent_graph = {}
		self.vertices = []
		self.maxH = 0
		
		# it is assumed that every path goes from 1 to x+1
		# so for loops are from 1 to x+1
		for x in range(1,int(verticeAmount)+1):
			self.adjacent_graph[x] = []
			self.vertices.append(x)
			
		self.distance = {}
		for x in range(1,int(verticeAmount)+1):
			self.distance[x] = INF
			
		self.pred = {}
		for x in range(1,int(verticeAmount)+1):
			self.pred[x] = None

		
#adds edge to the adjacent graph (x,y)		
def add_edge(g,x,y,wght):	
	g.adjacent_graph[x].append(EdgeNode(y,wght))
	g.adjacent_graph[y].append(EdgeNode(x,wght))	

#modified dijkstra algorithm
def dijkstra(g,s):
	
	for i in g.vertices:
		g.distance[i] = INF		#first assume that distance (or weight) to every
		g.pred[i] = 0			# node is infinite
		
	g.distance[s] = 0			#distance to starting point is 0
	
	queue = [i for i in g.vertices]		# add vertices to queue
	
	while len(queue) > 0:	
		minval = INF
		u = 0
		for vert in queue:
			if g.distance[vert] < minval:	#if minimum value is larger than that vertice
				minval = g.distance[vert]	# in queue, that becomes the new minval
				u = vert
		queue.remove(u)		#remove vertice from queue	
		
		for edge in g.adjacent_graph[u]:	
			v = edge.node
			if g.distance[v] > max(g.distance[u], edge.weight):		#instead of maintaining
				g.distance[v] = max(g.distance[u], edge.weight)		# the path length, we look
				g.pred[v] = u							# at the minimum edge weight in the path
				
		
def print_path(g,u):
	if g.pred[u] != 0:			#while all the path cities haven't been gone through
		print_path(g,g.pred[u])
	print("From:", g.pred[u], "to:", u,)
