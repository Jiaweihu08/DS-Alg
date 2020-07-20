#python3

class Edge:
	def __init__(self, fr, to, cap):
		self.fr = fr
		self.to = to
		self.cap = cap

	# def __repr__(self):
	# 	return f"{self.fr} -> {self.to}; w:{self.cap}\n"

class Vertex:
	def __init__(self, key):
		self.key = key
		self.dist = float('inf')
		self.prev_id = None
		self.edge_ids = []

	# def __repr__(self):
	# 	return 'V: {}'.format(self.key)


class Graph:
	def __init__(self):
		self.fc, self.cc = map(int, input().split())
		adj_matrix = [list(map(int, input().split())) for _ in range(self.fc)]
		self.s = self.fc + self.cc
		self.graph = [Vertex(i) for i in range(self.s + 2)]
		self.edges = []
		for to in range(self.fc):
			self.add_edge(self.s, to)
		for fr in range(self.fc, self.s):
			self.add_edge(fr, self.s + 1)
		self.add_bipartite_edges(adj_matrix)

	# def __init__(self, lines):
	# 	self.fc, self.cc = map(int, lines[0].split())
	# 	self.s = self.fc + self.cc
	# 	self.graph = [Vertex(i) for i in range(self.s + 2)]
	# 	self.edges = []
	# 	for to in range(self.fc):
	# 		self.add_edge(self.s, to)
	# 	for fr in range(self.fc, self.s):
	# 		self.add_edge(fr, self.s + 1)
	# 	adj_matrix = [list(map(int, line.split())) for line in lines[1:]]
	# 	self.add_bipartite_edges(adj_matrix)
		# print(self.edges)
		# print(self.graph)

	def add_edge(self, fr, to):
		forward_edge = Edge(fr, to, 1)
		backward_edge = Edge(to, fr, 0)
		self.graph[fr].edge_ids.append(len(self.edges))
		self.edges.append(forward_edge)
		self.graph[to].edge_ids.append(len(self.edges))
		self.edges.append(backward_edge)

	def add_bipartite_edges(self, adj_matrix):
		for i in range(self.fc):
			for j in range(self.cc):
				if adj_matrix[i][j]:
					self.add_edge(i, self.fc + j)

	def add_flow(self, id_, flow):
		self.edges[id_].cap -= flow
		self.edges[id_ ^ 1].cap += flow

	def add_result(self, edge_id, result):
		edge = self.edges[edge_id]
		if edge.to >= self.fc and edge.fr < self.fc:
			# print(edge)
			index = edge.fr
			val = edge.to - self.fc + 1
			result[index] = val

	def reset_vertex_values(self):
		for v in self.graph:
			v.dist = float('inf')
			v.prev_id = None
		self.graph[self.s].dist = 0

	def dijkstra(self):
		self.reset_vertex_values()
		q = self.graph[:]
		while q:
			node = min(q, key=lambda x: x.dist)
			q.remove(node)
			for edge_id in node.edge_ids:
				edge = self.edges[edge_id]
				to_node = self.graph[edge.to]
				if edge.cap > 0 and to_node.dist > node.dist + 1:
					to_node.dist = node.dist + 1
					to_node.prev_id = edge_id
					q.append(to_node)

	def find_best_path(self):
		self.dijkstra()
		s, u = self.s, len(self.graph) - 1
		path = []
		min_cap = float('inf')
		while u != s:
			edge_id = self.graph[u].prev_id
			if edge_id == None:
				return False, None
			path.append(edge_id)
			edge = self.edges[edge_id]
			edge_cap = edge.cap
			if edge_cap < min_cap:
				min_cap = edge_cap
			u = edge.fr
		return path, min_cap

	def max_flow(self):
		flow = 0
		result = [-1] * self.fc
		while True:
			path, min_cap = self.find_best_path()
			if not path:
				return result, flow
			for edge_id in path:
				self.add_flow(edge_id, min_cap)
				self.add_result(edge_id, result)
			flow += min_cap

if __name__ == '__main__':
# 	lines = '''2 2
# 1 1
# 1 0'''.split('\n')
	graph = Graph()
	print(*graph.max_flow()[0])
	