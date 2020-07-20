#python3


class Vertex:
	def __init__(self, key):
		self.key = key
		self.dist = float('inf')
		self.prev = None
		self.out_vertices = []

	def __repr__(self):
		return str(self.key)

class Edge:
	def __init__(self, fr, to, weight):
		self.fr = fr
		self.to = to
		self.weight = weight

	def relax(self):
		if self.to.dist > self.fr.dist + self.weight:
			self.to.dist = self.fr.dist + self.weight
			self.fr.prev = self.to
			return True
		return False

	def __repr__(self):
		return "edge: fr: {}, to: {}, weight: {}".format(self.fr, self.to, self.weight)

def optimal_exchange(graph, edges, s):
	n = len(graph)
	s.dist = 0
	for _ in range(n - 1):
		for edge in edges:
			edge.relax()
	
	cycle_vs = set()
	for edge in edges:
		relaxed = edge.relax()
		if relaxed:
			# print('----- relaxed -----', edge)
			cycle_vs.add(edge.to)
	
	while cycle_vs:
		u = cycle_vs.pop()
		for v in u.out_vertices:
			if v.dist != '-':
				v.dist = '-'
				cycle_vs.add(v)


def main():
	n, m = map(int, input().split())
	graph = [Vertex(key) for key in range(1, n + 1)]
	edges = []
	for _ in range(m):
		fr, to, weight = map(int, input().split())
		edge = Edge(graph[fr - 1], graph[to - 1], weight)
		edges.append(edge)
		graph[fr - 1].out_vertices.append(edge.to)
	s = graph[int(input()) - 1]

# 	lines = '''5 4
# 1 2 1
# 4 1 2
# 2 3 2
# 3 1 -5
# 4'''.split('\n')
# 	n, m = map(int, lines[0].split())
# 	graph = [Vertex(key) for key in range(1, n + 1)]
# 	edges = []
# 	for line in lines[1:-1]:
# 		fr, to, weight = map(int, line.split())
# 		edge = Edge(graph[fr - 1], graph[to - 1], weight)
# 		edges.append(edge)
# 		graph[fr - 1].out_vertices.append(edge.to)
# 	s = graph[int(lines[-1]) - 1]

	optimal_exchange(graph, edges, s)

	for vertex in graph:
		if vertex.dist == float('inf'):
			print('*')
		else:
			print(vertex.dist)


if __name__ == '__main__':
	main()


