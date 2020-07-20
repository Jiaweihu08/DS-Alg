#python3

class Vertex:
	def __init__(self, key):
		self.key = key
		self.dist = float('inf')
		self.prev = None
		self.edges = []

	def __repr__(self):
		return "vertex_{}; d:{}".format(self.key + 1, self.dist)

	def __lt__(self, other):
		return self.dist < other.dist

	def __eq__(self, other):
		return self.key == other.key

class Edge:
	def __init__(self, u, v, capacity, id_):
		self.u = u
		self.v = v
		self.capacity = capacity
		self.id = id_

	def relax(self):
		if self.capacity > 0 and self.v.dist > self.u.dist + 1:
			self.v.dist = self.u.dist + 1
			self.v.prev = self.u
			self.v.edge_id = self.id
			return True
		return False

	# def __eq__(self, other):
	# 	return self.u == other.u and self.v == other.v

	# def __lt__(self, other):
	# 	return self.capacity < other.capacity

	def __repr__(self):
		return "vertex {} -> {} - cap:{}".format(self.u.key + 1,
								self.v.key + 1,
								self.capacity)

def dijkstra(graph):
	q = graph[:]
	while q:
		u = min(q)
		q.remove(u)
		for edge in u.edges:
			if edge.v.key == 0 or edge.u.key == graph[-1].key:
				continue
			if edge.relax():
				q.append(edge.v)

def get_shortest_path(graph, edges):
	dijkstra(graph)
	s, u = graph[0], graph[-1]
	path = []
	min_cap = float('inf')
	while u != s:
		if not u.prev:
			return False, None
		name = "{}-{}-{}".format(u.prev.key, u.key, u.edge_id)
		edge = edges[name]
		path.append(edge)
		if edge.capacity < min_cap:
			min_cap = edge.capacity
		u = u.prev
	return path, min_cap

def max_flow(graph, edges):
	flow = 0
	while True:
		path, min_cap = get_shortest_path(graph, edges)
		if not path:
			return flow
		for edge in path:
			edge.capacity -= min_cap
			reversed_edge = edges["{}-{}-{}".format(edge.v.key, edge.u.key, edge.id ^ 1)]
			reversed_edge.capacity += min_cap
		for vertex in graph[1:]:
			vertex.dist = float('inf')
			vertex.prev = None
		flow += min_cap

def read_data():
	vertex_count, edge_count = map(int, input().split())
	graph = [Vertex(i) for i in range(vertex_count)]
	graph[0].dist = 0
	edges = {}
	id_ = 0
	for _ in range(edge_count):
		u, v, capacity = map(int, input().split())
		u, v = u - 1, v - 1
		edge = Edge(graph[u], graph[v], capacity, id_)
		reversed_edge = Edge(graph[v], graph[u], 0, id_ + 1)
		graph[u].edges.extend([edge, reversed_edge])
		name_1 = "{}-{}-{}".format(u, v, id_)
		name_2 = "{}-{}-{}".format(v, u, id_ + 1)
		edges[name_1] = edge
		edges[name_2] = reversed_edge
		id_ += 2
		

# 	lines = '''8 9
# 1 2 5
# 1 3 20
# 2 5 5
# 2 6 5
# 3 4 20
# 4 5 20
# 5 8 20
# 6 7 5
# 7 8 5'''.split('\n')

# 	vertex_count, edge_count = map(int, lines[0].split())
# 	graph = [Vertex(i) for i in range(vertex_count)]
# 	graph[0].dist = 0
# 	edges = {}
# 	id_ = 0
# 	for line in lines[1:]:
# 		u, v, capacity = map(int, line.split())
# 		u, v = u - 1, v - 1
# 		edge = Edge(graph[u], graph[v], capacity, id_)
# 		reversed_edge = Edge(graph[v], graph[u], 0, id_ + 1)
# 		graph[u].edges.extend([edge, reversed_edge])
# 		name_1 = "{}-{}-{}".format(u, v, id_)
# 		name_2 = "{}-{}-{}".format(v, u, id_ + 1)
# 		edges[name_1] = edge
# 		edges[name_2] = reversed_edge
# 		id_ += 2

	# print(graph)
	# print(edges)
	return graph, edges

if __name__ == '__main__':
	graph, edges = read_data()
	print(max_flow(graph, edges))