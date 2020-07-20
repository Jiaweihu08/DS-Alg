#python3

from math import sqrt
from itertools import combinations, product
from random import randint
from time import process_time


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

	def __repr__(self):
		return str(self.position)

	def __eq__(self, other):
		return self.position == other.position


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
		return '{} --> {}; dist:{}\n'.format(self.fr, self.to, self.dist)


# ----------------------------------------------------
def dist(a, b):
		x = pow(a[0] - b[0], 2)
		y = pow(a[1] - b[1], 2)
		return sqrt(x + y)

def testing(points, n, k):
	s = max(max([dist(points[i], points[j]) for j in range(n)]) for i in range(n))
	answer = 0
	print('computing naive answer')
	for partition in product(range(k), repeat=n):
		min_dist = s
		for i in range(n):
			for j in range(n):
				if partition[i] != partition[j]:
					min_dist = min(min_dist, dist(points[i], points[j]))
		answer = max(answer, min_dist)

	return answer

def generate_test_cases():
	n = randint(7, 10)
	vertices = []
	points = []
	for _ in range(n):
		a, b = randint(0, 10), randint(0, 10)
		vertices.append(Vertex((randint(0, 10), randint(0, 10))))
		points.append((a, b))
	k = randint(3, n-2)

	print('n, k:', n, k)
	print(vertices)

	return n, vertices, points, k



def clustering():
	lines = '''8
3 1
1 2
4 6
9 8
9 9
8 9
3 11
4 12
4'''.split('\n')
	n = int(lines[0])
	vertices = [Vertex(tuple(map(int, line.split()))) for line in lines[1:-1]]
	k = int(lines[-1])

	points = [tuple(map(int, line.split())) for line in lines[1:-1]]
	

	# n, vertices, points, k = generate_test_cases()
	# t1 = process_time()
	
	naive_answer = testing(points, n, k)
	# print('naive answer process time:'.format(process_time() - t1))
	print('naive answer !!!', naive_answer)

	# n = int(input())
	# vertices = [Vertex(tuple(map(int, input().split()))) for _ in range(n)]
	# k = int(input())

	edges = [Edge(vertices[i], vertices[j]) for i, j in combinations(range(n), 2)]
	edges = sorted(edges, key=lambda x: x.dist)
	print(edges)

	for _ in range(len(edges)):
		edge = edges.pop(0)
		if edge.fr.find() != edge.to.find():
			edge.fr.union(edge.to)
			n -= 1
			if n == k:
				print('breaking')
				break
	
	for edge in edges:
		if edge.fr.find() != edge.to.find():
			print(edge)
			return edge.dist == naive_answer
		else:
			print('not -----', edge)

if __name__ == '__main__':
	print(clustering())


