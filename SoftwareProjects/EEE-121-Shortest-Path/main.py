import os
import math

# Implementation of a Node containing the name of the POI 
class Node:
	def __init__(self, name: str):
		self.name = name
# Implementation of and Edge with the the distance and cost between two POIs
class Edge:
	def __init__(self, distance: int, cost: int, POIs: (str,str)):
		self.distance = distance
		self.cost = cost
		self.POIs = POIs

# Implementation of Minimum Heap taken from Week11 Module
class MinHeap:
    def __init__(self) -> None:
        self.size = 0
        self.keys = [None]  # other elements start at index 1
        self.values = [None]
    
    def __str__(self) -> str:
        return f"keys: {self.keys}, values: {self.values}"

    def add(self, item: int, value: int) -> None:
        self.keys.append(item)
        self.values.append(value)
        self.size += 1
        
        idx = self.size
        parent_idx = idx//2
        while (idx > 1) and (self.values[parent_idx] > value):
            self._swap_nodes(parent_idx, idx)
            idx = parent_idx
            parent_idx = idx//2

    def _swap_nodes(self, idx1: int, idx2: int):
        # Swap keys
        self.keys[idx1], self.keys[idx2] = self.keys[idx2], self.keys[idx1]

        # Swap values
        self.values[idx1], self.values[idx2] = self.values[idx2], self.values[idx1]

    def get_smallest(self) -> int:
        """Return the key of the Node with smallest value"""
        return self.keys[1]

    def remove_smallest(self) -> int:
        """Remove and return the key of Node with smallest value"""
        key_of_min = self.keys[1]
        end_key = self.keys.pop()
        end_value = self.values.pop()
        self.size -= 1

        if self.size:
            self.keys[1] = end_key
            self.values[1] = end_value

        # Reorder the heap to fix order
        self._reorder_heap_from_root()
        
        return key_of_min

    def _reorder_heap_from_root(self):
        parent_idx = 1
        while True:
            right_idx = parent_idx*2 + 1
            left_idx = parent_idx*2

            # Get index with minimum value among parent and children
            min_idx = parent_idx
            if left_idx <= self.size:
                if self.values[left_idx] < self.values[min_idx]:
                    min_idx = left_idx
            if right_idx <= self.size:
                if self.values[right_idx] < self.values[min_idx]:
                    min_idx = right_idx
            
            # If parent already minimum value, heap already ok.
            # Otherwise, swap and continue
            if min_idx == parent_idx:
                break
            self._swap_nodes(min_idx, parent_idx)
            parent_idx = min_idx

# Undirected Graph implementation taken and modified from Week11 Module
class GraphUndirected:
	def __init__(self, vertices: list) -> None:
		self.num_vertices = len(vertices)
		self.vertices = vertices
		self.num_edges = 0
		self.adj_list = {} 
		for v in vertices:
		    self.adj_list[v.name] = []
    
	def __str__(self) -> str:
	    return f"adj: {self.adj_list}"

	def add_edge(self, edge: Edge) -> None:
		self.adj_list[edge.POIs[0]].append([edge.POIs[1], edge.cost, edge.distance])
		self.adj_list[edge.POIs[1]].append([edge.POIs[0], edge.cost, edge.distance])
		self.num_edges += 1

	def adj(self, v: str): 
	    return self.adj_list[v] # returns vertices adjacent to v
	
	def has_edge(self, v: str, w: str) -> bool:
	    if w in self.adj_list[v]:
	        return True
	    return False
	
	def get_cost(self, v: str, w: str) -> int:
		for edge in self.adj_list[v]:
			if edge[0] == w:
				return edge[1]

	def get_dist(self, v: str, w: str) -> int:
		for edge in self.adj_list[v]:
			if edge[0] == w:
				return edge[2]

# Implentation of Dijkstra's Algorithm taken and modified from Week11 Module
class Dijkstra:
	def __init__(self, graph: GraphUndirected, init_v: str) -> None:
		self.graph = graph
		self.source = init_v
		self.dist_to, self.edge_to, self.is_marked = {}, {}, {}
		for v in self.graph.vertices:
			self.dist_to[v.name] = float('inf') 
			self.edge_to[v.name] = None
			self.is_marked[v.name] = False
		self.dist_to[init_v] = 0
		self.shortest_path(self.graph)

	def shortest_path(self, graph: GraphUndirected) -> None:
		pq = MinHeap()
		pq.add(self.source, 0)  # Set distance to source as 0
		
		# Set distance to other vertices to be inf in PQ
		for v in graph.vertices:
			if v.name != self.source:
				pq.add(v.name, float('inf'))

		p1 = pq.remove_smallest()
		self.scan(graph, pq, p1)
		while pq.size > 0:
			p1 = pq.remove_smallest()
			if self.is_marked[p1]:
				continue
			self.scan(graph, pq, p1)

	def scan(self, graph: GraphUndirected, pq: MinHeap,point: int) -> None:
		self.is_marked[point] = True
		for neighbor, _ , distance in graph.adj(point):
			if self.is_marked[neighbor]:
				continue
			if self.dist_to[neighbor] > self.dist_to[point] + distance:
				self.dist_to[neighbor] = self.dist_to[point] + distance 
				self.edge_to[neighbor] = point
				pq.add(neighbor, self.dist_to[point] + distance)

	def get_shortest_path(self, dest):
		start = self.source
		end = dest
		path = []
		while end != start:
			path.append(end)
			end = self.edge_to[end]

		path.append(start)
		path.reverse()

		return self.dist_to[dest], path

# Implentation of Prim's Algorithm taken and modified from Week12 Module
class PrimMST:
	def __init__(self, graph: GraphUndirected, init_v: str) -> None:
		self.graph = graph
		self.source = init_v
		self.dist_to, self.edge_to, self.is_marked = {}, {}, {}
		for v in self.graph.vertices:
			self.dist_to[v.name] = float('inf') 
			self.edge_to[v.name] = None
			self.is_marked[v.name] = False
		self.dist_to[init_v] = 0
		self.mst = []

		self.prim(self.graph)

	def get_mst(self) -> list[set]:
		unique = []
		seen = []
		for edge in self.mst:
			if edge.POIs not in seen:
				seen.append(edge.POIs)
				unique.append(edge)
		self.mst = unique
		return self.mst 

	def prim(self, graph: GraphUndirected):
		pq = MinHeap()
		pq.add(self.source, 0)  # Set distance to source as 0
		
		# Set distance to other vertices to be inf in PQ
		for v in graph.vertices:
		    if v.name != self.source:
		        pq.add(v.name, float('inf'))
		
		p1 = pq.remove_smallest()
		self.scan(graph, pq, p1)
		while pq.size > 0:
			p1 = pq.remove_smallest()
			if self.is_marked[p1]:
				dist = graph.get_dist(p1, self.edge_to[p1])
				cost = graph.get_cost(p1, self.edge_to[p1])
				self.mst.append(Edge(dist, cost, (p1, self.edge_to[p1])))
				continue
			self.scan(graph, pq, p1)

	def scan(self, graph: GraphUndirected, pq: MinHeap, point: str):
		self.is_marked[point] = True
		for neighbor, cost, _ in graph.adj(point):
			if self.is_marked[neighbor]:
			    continue
			if self.dist_to[neighbor] > cost:
			    self.dist_to[neighbor] = cost 
			    self.edge_to[neighbor] = point
			    pq.add(neighbor, cost)

def main():
	""" Input-parsing """
	# Reads the first line of the input
	V, E = input('').rstrip('\r\n').split()
	V, E = int(V), int(E)

	# Reads all the input for all V POIs
	nodes = input('').rstrip('\r\n').split()
	nodes = nodes[:V]
	# Make the inputs into Nodes
	for i in range(len(nodes)):
		nodes[i] = Node(nodes[i])
	
	# Initializes the graph of Scenario 2 by adding all nodes
	scenario2 = GraphUndirected(nodes)

	# Reads all the input for E routes and adds them to the graph
	# also, calculates the total cost for Scenario 2
	C2 = 0
	for _ in range(E):
		e = input('').rstrip('\r\n').split()
		edge = Edge(int(e[2]), int(e[3]), (e[0],e[1]))
		scenario2.add_edge(edge)
		C2 += edge.cost

	# Reads the input for the X tests to be made
	X = int(input(''))
	tests = []
	for _ in range(X):
		route = input('').rstrip('\r\n').split() 
		tests.append((route[0],route[1]))
	
	""" Generate Scenario 1 """ 
	# Finds the subset of routes
	subset = PrimMST(scenario2, nodes[0].name).get_mst()

	# Builds the graph
	scenario1 = GraphUndirected(nodes)
	
	# Adds the edges to the graph of Scenario 1
	# also, finds the total cost to build
	C1 = 0
	for route in subset:
		scenario1.add_edge(route)
		C1 += scenario1.get_cost(route.POIs[0], route.POIs[1])

	""" Testing both scenarios """
	results = []
	for src, dest in tests: 
		# Finds the SPT for Scenario 1 
		sp1 = Dijkstra(scenario1, src) 
		d1 = sp1.get_shortest_path(dest) 
		# Finds the SPT for Scenario 2
		sp2 = Dijkstra(scenario2, src) 
		d2 = sp2.get_shortest_path(dest)
		# Append the lines
		line1 = [d1[0], d2[0], d1[0]-d2[0]]
		line2 = d1[1]
		line3 = d2[1]
		results.append([line1, line2, line3])

	""" Displaying the output """
	# Displays the cost for Scenario 1 and Scenario 2
	print(C1, C2)	
	# Displays the output for the number of subroutes
	print(len(subset))
	# Displays the subroutes generated in Scenario 2	
	for routes in subset:
		print(routes.POIs[0], routes.POIs[1])
	# Displays the results for the test routes between two POIs
	for i in results:
		print(i[0][0], i[0][1], i[0][2]) 
		print(*i[1])
		print(*i[2])	

if __name__ == '__main__':
	main()