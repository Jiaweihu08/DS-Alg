#python3

from math import sqrt
from itertools import combinations


class Vertex:
	def __init__(self, position):
		self.position = position
		self.make_set()

	def make_set(self):
		self.parent = self
		self.rank = 0

	def find(self):
		if self.parent != self:
			self.parent = self.parent.find()
		return self.parent

	def union(self, other):
		src_self = self.find()
		src_other = other.find()
		if src_self == src_other:
			return
		if src_self.rank > src_other.rank:
			src_other.parent = src_self
		else:
			src_self.parent = src_other
			if src_self.rank == src_other.rank:
				src_other.rank = src_self.rank + 1

	def __eq__(self, other):
		return self.position == other.position

	def __repr__(self):
		return str(self.position)

class Edge:
	def __init__(self, fr, to):
		self.fr = fr
		self.to = to
		self.dist()

	def dist(self):
		x = pow(self.fr.position[0] - self.to.position[0], 2)
		y = pow(self.fr.position[1] - self.to.position[1], 2)
		self.dist = sqrt(x + y)

	def __repr__(self):
		return '{} - {}: {}\n'.format(self.fr, self.to, self.dist)

def kruskal_min_dist():
	lines = '''9
0 0
1 1
2 -3
3 6
4 -4
5 8
6 -7
7 12
8 -11'''.split('\n')
	n = int(lines[0])
	vertices = [Vertex(tuple(map(int, line.split()))) for line in lines[1:]]

	# n = int(input())
	# vertices = [Vertex(tuple(map(int, input().split()))) for _ in range(n)]

	edges = [Edge(vertices[i], vertices[j]) for i, j in combinations(range(n), 2)]
	edges = sorted(edges, key=lambda x: x.dist)

	cost = 0
	for edge in edges:
		if edge.fr.find() != edge.to.find():
			cost += edge.dist
			edge.fr.union(edge.to)
	return cost




if __name__ == '__main__':
	print("{:.7f}".format(kruskal_min_dist()))


