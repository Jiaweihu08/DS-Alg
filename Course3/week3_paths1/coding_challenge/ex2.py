#python3


class Vertex:
	def __init__(self, key):
		self.key = key
		self.color = None
		self.visited = False
		self.reachables = []
		
	def __eq__(self, other):
		return self.key == other.key

	def __repr__(self):
		return str(self.key)

def bfs(graph):
	for v in graph:
		if v.visited:
			continue
		v.visited = True
		v.color = 1
		q = [v]
		while q:
			cur_v = q.pop(-1)
			color = 1 - cur_v.color
			for adj_v in cur_v.reachables:
				if not adj_v.visited:
					adj_v.visited = True
					adj_v.color = color
					q = [adj_v] + q
				elif adj_v.color == cur_v.color:
					return 0		
	return 1


def main():
	n, m = map(int, input().split())
	graph = [Vertex(key) for key in range(1, n + 1)]
	for _ in range(m):
		fr, to = map(int, input().split())
		graph[fr - 1].reachables.append(graph[to - 1])
		graph[to - 1].reachables.append(graph[fr - 1])

# 	inputs = '''5 4
# 5 2
# 4 2
# 3 4
# 1 4'''.split('\n')
# 	n, m = map(int, inputs[0].split())
# 	graph = [Vertex(key) for key in range(1, n + 1)]
# 	for edge in inputs[1:]:
# 		fr, to = map(int, edge.split())
# 		graph[fr - 1].reachables.append(graph[to - 1])
# 		graph[to - 1].reachables.append(graph[fr - 1])

	is_bipartite = bfs(graph)
	return is_bipartite



if __name__ == '__main__':
	print(main())
