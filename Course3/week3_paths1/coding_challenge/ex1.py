#python3


class Vertex:
	def __init__(self, key):
		self.key = key
		self.reachables = []
		self.dist = float('inf')
		self.prev = None

	def __eq__(self, other):
		return self.key == other.key

	# def __repr__(self):
	# 	return str(self.key)

def bfs(graph, s):
	s.dist = 0
	q = [s]
	while q:
		u = q.pop(-1)
		for v in u.reachables:
			if v.dist == float('inf'):
				q = [v] + q
				v.dist = u.dist + 1
				v.prev = u

def get_path_length(v, u):
	path_length = 0
	while u != v:
		path_length += 1
		if u.prev:
			u = u.prev
		else:
			return -1
	return path_length

def main():
	n, m = map(int, input().split())
	graph = [Vertex(key) for key in range(1, n + 1)]
	for _ in range(m):
		fr, to = map(int, input().split())
		graph[fr - 1].reachables.append(graph[to - 1])
		graph[to - 1].reachables.append(graph[fr - 1])
	u, v = map(int, input().split())

# 	inputs = '''4 4
# 1 2
# 4 1
# 2 3
# 3 1
# 2 4'''.split('\n')
# 	n, m = map(int, inputs[0].split())
# 	graph = [Vertex(key) for key in range(1, n + 1)]
# 	for edge in inputs[1:-1]:
# 		fr, to = map(int, edge.split())
# 		graph[fr - 1].reachables.append(graph[to - 1])
# 		graph[to - 1].reachables.append(graph[fr - 1])
# 	u, v = map(int, inputs[-1].split())

	u = graph[u - 1]
	v = graph[v - 1]

	bfs(graph, v)
	path_length = get_path_length(v, u)

	return path_length


if __name__ == '__main__':
	print(main())




