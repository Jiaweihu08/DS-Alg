#python3

class Edge:
	def __init__(self, fr, to, cap):
		self.fr = fr
		self.to = to
		self.cap = cap

	def __repr__(self):
		return f"{self.fr + 1} -> {self.to + 1}; w:{self.cap}"

class Vertex:
	def __init__(self, key):
		self.key = key
		self.dist = float('inf')
		self.prev_id = None
		self.edge_ids = []


class Graph:
	# def __init__(self):
	# 	n, m = map(int, input().split())
	# 	self.graph = [[] for _ in range(n)]
	# 	for _ in range(m):
	# 		fr, to, cap = map(int, input().split())
	# 		fr, to = fr - 1, to - 1
	# 		self.graph[fr].append(Edge(fr, to , cap))

	def __init__(self, lines):
		n, m = map(int, lines[0].split())
		self.edges = []
		self.graph = [Vertex(i) for i in range(n)]
		for line in lines[1:]:
			fr, to, cap = map(int, line.split())
			self.add_edge(fr - 1, to - 1, cap)

	def add_edge(self, fr, to, cap):
		forward_edge = Edge(fr, to, cap)
		backward_edge = Edge(to, fr, 0)
		self.graph[fr].edge_ids.append(len(self.edges))
		self.edges.append(forward_edge)
		self.graph[to].edge_ids.append(len(self.edges))
		self.edges.append(backward_edge)

	def add_flow(self, id_, flow):
		self.edges[id_].cap -= flow
		self.edges[id_ ^ 1].cap += flow

	def reset_vertex_values(self):
		for v in self.graph:
			v.dist = float('inf')
			v.prev_id = None
		self.graph[0].dist = 0

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
		s, u = 0, len(self.graph) - 1
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
		while True:
			path, min_cap = self.find_best_path()
			if not path:
				return flow
			for edge_id in path:
				self.add_flow(edge_id, min_cap)
			flow += min_cap

if __name__ == '__main__':
	lines = '''5 7
1 2 2
2 5 5
1 3 6
3 4 2
4 5 1
3 2 3
2 4 1'''.split('\n')
	graph = Graph(lines)
	print(graph.max_flow())
	






