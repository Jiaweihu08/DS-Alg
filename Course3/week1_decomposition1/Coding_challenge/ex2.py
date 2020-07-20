#python3
import sys

class Vertex:
	def __init__(self, key):
		self.key = key
		self.visited = False
		self.adj_vertex = []

	def explore(self):
		self.visited = True
		for v in self.adj_vertex:
			if not v.visited:
				v.explore()

def main():
	lines = sys.stdin.read().strip().split('\n')
# 	lines = '''4 4
# 1 2
# 3 2
# 4 3
# 1 4'''.split('\n')
	n, m = map(int, lines[0].split())
	vertices = [Vertex(key) for key in range(1, n + 1)]

	for line in lines[1:]:
		fr, to = map(int, line.split())
		vertices[fr - 1].adj_vertex.append(vertices[to - 1])
		vertices[to - 1].adj_vertex.append(vertices[fr - 1])

	count = 0
	for v in vertices:
		if not v.visited:
			v.explore()
			count += 1
	print(count)



if __name__ == '__main__':
	main()