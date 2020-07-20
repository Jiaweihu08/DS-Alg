#python3

from itertools import combinations
from math import sqrt
from random import choice

class Vertex:
	def __init__(self, position):
		self.position = position
		self.dist = float('inf')
		self.parent = None
		self.edges = set()

	def __repr__(self):
		return str(self.position)

	def __lt__(self, other):
		return self.dist < other.dist

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
		return '{} --> {}; dist: {}\n'.format(self.fr, self.to, self.dist)

def prim():
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

	for i, j in combinations(range(n), 2):
		vertices[i].edges.add(Edge(vertices[i], vertices[j]))
		vertices[j].edges.add(Edge(vertices[j], vertices[i]))

	u = vertices[0]
	u.dist = 0
	q = set(vertices)
	cost = 0
	while q:
		v = min(q)
		q.remove(v)
		cost += v.dist
		for edge in v.edges:
			if edge.to in q and edge.to.dist > edge.dist:
				edge.to.dist = edge.dist
				# edge.to.parent = v
	return cost



if __name__ == '__main__':
	print('{:.7f}'.format(prim()))



