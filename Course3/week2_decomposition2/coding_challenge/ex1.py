#python3

count = 1

class Vertex:
	def __init__(self, key):
		self.key = key
		self.visited = False
		self.reachables = []
		self.prev = None
		self.post = None

	def search(self):
		global count
		self.visited = True
		self.prev = count
		count += 1
		for v in self.reachables:
			if not v.visited:
				is_cycle = v.search()
				if is_cycle:
					return 1
			elif v.post == None:
				return 1
	
		self.post = count
		count += 1
		return 0


def main():
	
# 	ops = '''5 7
# 1 2
# 2 3
# 1 3
# 3 4
# 1 4
# 2 5
# 3 5'''.split('\n')
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
		is_cycle = v.search()
		if is_cycle == 1:
			return 1
	return 0



if __name__ == '__main__':
	print(main())

