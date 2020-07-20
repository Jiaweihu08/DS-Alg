#python3

count = 1

class Vertex:
	def __init__(self, key):
		self.key = key
		self.visited = False
		self.reachables = []
		self.post = None

	def search(self):
		self.visited = True
		global count
		count += 1
		for v in self.reachables:
			if not v.visited:
				v.search()
		self.post = count
		count += 1

	def __repr__(self):
		return str(self.key)

def main():
# 	ops = '''4 3
# 1 2
# 4 1
# 3 1'''.split('\n')
# 	n, m = map(int, ops[0].split())
# 	vertices = [Vertex(key) for key in range(1, n + 1)]
# 	for op in ops[1:]:
# 		u, v = map(int, op.split())
# 		vertices[u - 1].reachables.append(vertices[v - 1])

	n, m = map(int, input().split())
	vertices = [Vertex(key) for key in range(1, n + 1)]
	for _ in range(m):
		u, v = map(int, input().split())
		vertices[u - 1].reachables.append(vertices[v - 1])

	for v in vertices:
		if not v.visited:
			v.search()

	print(*reversed(sorted(vertices, key=lambda v: v.post)))



if __name__ == '__main__':
	main()