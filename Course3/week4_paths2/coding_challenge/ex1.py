#python3

class Vertex:
	def __init__(self, key):
		self.key = key
		self.dist = float('inf')
		self.prev = None
		self.out_edges = []

	def __repr__(self):
		return str(self.key) + ', ' + str(self.dist)

	def __lt__(self, other):
		return self.dist < other.dist

class DirectedEdge:
	def __init__(self, fr, to, weight):
		self.fr = fr
		self.to = to
		self.weight = weight

	def relax(self):
		if self.to.dist > self.fr.dist + self.weight:
			self.to.dist = self.fr.dist + self.weight
			self.to.prev = self.fr
			return True
		return False

# class PriorityQueue:
# 	def __init__(self, graph):
# 		self.graph = graph
# 		self.build_queue(graph)

# 	def __repr__(self):
# 		return str(self.graph)

# 	def build_queue(self, graph):
# 		n = len(self.graph) // 2
# 		for i in reversed(range(n)):
# 			self.sift_down(i)

# 	def sift_down(self, i):
# 		n = len(self.graph)
# 		while i < n // 2:
# 			indice = i
# 			l = i * 2 + 1
# 			if l < n and self.graph[l] < self.graph[indice]:
# 				indice = l
# 			r = i * 2 + 2
# 			if r < n and self.graph[r] < self.graph[indice]:
# 				indice = r
# 			if indice != i:
# 				self.graph[i], self.graph[indice] = self.graph[indice], self.graph[i]
# 				i = indice
# 			else:
# 				break

# 	def sift_up(self, i):
# 		while i > 0:
# 			p = (i + 1) // 2 - 1
# 			if p >= 0 and self.graph[p] > self.graph[i]:
# 				self.graph[p], self.graph[i] = self.graph[i], self.graph[p]
# 				i = p
# 			else:
# 				break

# 	def insert(self, node):
# 		self.graph.append(node)
# 		self.sift_up(len(self.graph) - 1)

# 	def extract_min(self):
# 		# print('graph length', len(self.graph))
# 		self.graph[0], self.graph[-1] = self.graph[-1], self.graph[0]
# 		out = self.graph.pop()
# 		self.sift_down(0)
# 		return out

# 	def empty(self):
# 		return not bool(self.graph)


def dijkstra(graph, s):
	s.dist = 0
	q = set(graph)
	# q = PriorityQueue(graph)
	while q:#not q.empty():
		# v = q.extract_min()
		v = min(q)
		q.remove(v)
		for edge in v.out_edges:
			if edge.relax():
				q.add(edge.to)
				# q.insert(edge.to)

def main():
	# n, m = map(int, input().split())
	# graph = [Vertex(key) for key in range(1, n + 1)]
	
	# edges = []
	# for _ in range(m):
	# 	fr, to, weight = map(int, input().split())
	# 	edge = DirectedEdge(graph[fr - 1], graph[to - 1], weight)
	# 	graph[fr - 1].out_edges.append(edge)
	# u, v = map(int, input().split())
	# u, v = graph[u - 1], graph[v - 1]
	
	lines = '''4 4
1 2 1
4 1 2
2 3 2
1 3 5
1 3'''.split('\n')
	n, m = map(int, lines[0].split())
	graph = [Vertex(key) for key in range(1, n + 1)]
	edges = []
	for line in lines[1:-1]:
		fr, to, weight = map(int, line.split())
		edge = DirectedEdge(graph[fr - 1], graph[to - 1], weight)
		graph[fr - 1].out_edges.append(edge)
	u, v = map(int, lines[-1].split())
	u, v = graph[u - 1], graph[v - 1]

	dijkstra(graph, u)
	
	if v.dist == float('inf'):
		return -1
	else:
		return v.dist



if __name__ == '__main__':
	print(main())