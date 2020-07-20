#python3
import sys

sys.setrecursionlimit(200000)
count = 1

class Vertex:
	def __init__(self, key):
		self.key = key
		self.visited = False
		self.reachables = []
		
		self.reversed_visited = False
		self.reversed_reachables = []
		self.post = None
		# self.prev = None

	def explore(self, reversed=True):
		if reversed:
			global count
			self.reversed_visited = True
			# self.prev = count
			count += 1
			for v in self.reversed_reachables:
				if not v.reversed_visited:
					v.explore()
			self.post = count
			count += 1
		else:
			self.visited = True
			for v in self.reachables:
				if not v.visited:
					v.explore(reversed=False)

	def __repr__(self):
		return str(self.key)

def scc(graph):
	for v in graph:
		if not v.reversed_visited:
			v.explore()

	num_scc = 0
	new_graph = reversed(sorted(graph, key=lambda v: v.post))
	for v in new_graph:
		if not v.visited:
			v.explore(reversed=False)
			num_scc += 1
	return num_scc

def main():
	n, m = map(int, input().split())
	graph = [Vertex(key) for key in range(1, n + 1)]
	for _ in range(m):
		u, v = map(int, input().split())
		graph[u - 1].reachables.append(graph[v - 1])
		graph[v - 1].reversed_reachables.append(graph[u - 1])
	
# 	ops = '''5 7
# 2 1
# 3 2
# 3 1
# 4 3
# 4 1
# 5 2
# 5 3'''.split('\n')
# 	n, m = map(int, ops[0].split())
# 	graph = [Vertex(key) for key in range(1, n + 1)]
# 	for op in ops[1:]:
# 		u, v = map(int, op.split())
# 		graph[u - 1].reachables.append(graph[v - 1])
# 		graph[v - 1].reversed_reachables.append(graph[u - 1])

	num_scc = scc(graph)
	return num_scc




if __name__ == '__main__':
	print(main())