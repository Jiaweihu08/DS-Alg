#python3
import sys

class Vertex:
	def __init__(self, key):
		self.key = key
		self.visited = False
		self.adj_vertex = []

	def reach(self, v):
		self.visited = True
		for vertex in self.adj_vertex:
			if vertex.key == v:
				return 1
			if not vertex.visited:
				out = vertex.reach(v)
				if out == 1:
					return out
		return 0

def main():

# 	lines = '''4 2
# 1 2
# 3 2
# 1 4'''.split('\n')
	
	lines = sys.stdin.read().strip().split('\n')
	# print(lines)
	n, m = map(int, lines[0].split())
	vertices = [Vertex(key) for key in range(1, n + 1)]
	for line in lines[1:-1]:
		fr, to = map(int, line.split())
		vertices[fr - 1].adj_vertex.append(vertices[to - 1])
		vertices[to - 1].adj_vertex.append(vertices[fr - 1])
	
	u, v = map(int, lines[-1].split())
	is_reachable = vertices[u - 1].reach(v)
	return is_reachable


if __name__ == '__main__':
	print(main())