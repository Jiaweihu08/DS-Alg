#python3

class Vertex:
	def __init__(self, key):
		self.key = key
		self.dist = float('inf')
		self.prev = None
		# self.out_edges = []

	# def __repr__(self):
	# 	return f'vertex_{self.key}'

class Edge:
	def __init__(self, fr, to, weight):
		self.fr = fr
		self.to = to
		self.weight = weight

	def relax(self):
		# print(f'fr.dist: {self.fr.dist}, to.dist: {self.to.dist}\n')
		if self.to.dist > self.fr.dist + self.weight:
			self.to.dist = self.fr.dist + self.weight
			self.to.prev = self.fr
			return True
		return False

	# def __repr__(self):
	# 	return f'edge: {self.fr} --> {self.to} | weight: {self.weight}'

def negative_cycle(graph, edges):
	n = len(graph)
	i = 0
	for s in graph:
		i += 1
		# print(s)
		# print('-'*20)
		if s.dist == float('inf'):
			s.dist = 0
		for edge in edges:
			# print(edge)
			relaxed = edge.relax()
			if i == n and relaxed:
				# print('stopping here')
				return 1
	return 0

def main():
	n, m = map(int, input().split())
	graph = [Vertex(key) for key in range(1, n + 1)]
	edges = []
	for _ in range(m):
		fr, to, weight = map(int, input().split())
		edge = Edge(graph[fr - 1], graph[to - 1], weight)
		edges.append(edge)
		# graph[fr - 1].out_edges.append(edge)

# 	lines = '''4 4
# 1 2 1
# 2 4 -4
# 2 3 -1
# 4 1 2'''.split('\n')
# 	n, m = map(int, lines[0].split())
# 	graph = [Vertex(key) for key in range(1, n + 1)]
# 	edges = []
# 	for line in lines[1:]:
# 		fr, to, weight = map(int, line.split())
# 		edge = Edge(graph[fr - 1], graph[to - 1], weight)
		# graph[fr - 1].out_edges.append(edge)
# 		edges.append(edge)
	return negative_cycle(graph, edges)



if __name__ == '__main__':
	print(main())
