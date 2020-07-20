#python3

from __future__ import print_function
import sys
import threading
sys.setrecursionlimit(10**6)
threading.stack_size(2**26)


count = 1
scc_count = 1
scc_id = 0

class Vertex:
	def __init__(self, key):
		self.key = key
		self.visited = False
		self.scc = None
		self.reachables = []

		self.reverse_visited = False
		self.reverse_reachables = []
		# self.prev_order = None
		self.post_order = None

		self.val = None

	def explore(self, r=True, sccs=None):
		if r:
			global count
			self.reverse_visited = True
			# self.prev_order = count
			count += 1
			for v in self.reverse_reachables:
				if not v.reverse_visited:
					v.explore()
			self.post_order = count
			count += 1
		else:
			global scc_id

			self.scc = scc_id
			self.visited = True
			sccs[scc_id].append(self)
			for v in self.reachables:
				if not v.visited:
					v.explore(r=False, sccs=sccs)
	
	# def __repr__(self):
	# 	return 'Vertex_{}, val: {}'.format(self.key, self.val)

class MetaVertex:
	def __init__(self, scc, vertices):
		self.scc = scc
		self.vertices = vertices
		self.reachables = set()
		self.visited = False
		self.post = None

	def explore(self):
		global scc_count

		self.visited = True
		scc_count += 1
		for w in self.reachables:
			if not w.visited:
				w.explore()
		self.post = scc_count
		scc_count += 1
	
	# def __repr__(self):
	# 	return 'Metavertex: {}, reachables: {}'.format(self.scc, self.reachables)

def get_pos(num):
	if num > 0:
		return (num - 1) * 2, (num - 1) * 2 + 1
	return (-num - 1) * 2 + 1, (-num - 1) * 2

def read_inputs(lines):
	vertex_count, clause_count = map(int, lines[0].split())
	
	graph = []
	for key in range(1, vertex_count + 1):
		graph.append(Vertex(key))
		graph.append(Vertex(-key))

	for line in lines[1:]:
		c1, c2 = map(int, line.split())
		pos_c1, pos_neg_c1 = get_pos(c1)
		pos_c2, pos_neg_c2 = get_pos(c2)
		# print(c1, c2)
		# print(pos_c1, pos_neg_c1, pos_c2, pos_neg_c2)
		graph[pos_neg_c1].reachables.append(graph[pos_c2])
		graph[pos_c2].reverse_reachables.append(graph[pos_neg_c1])
		graph[pos_neg_c2].reachables.append(graph[pos_c1])
		graph[pos_c1].reverse_reachables.append(graph[pos_neg_c2])

	return clause_count, vertex_count, graph

def is_satisfiable():
	lines = sys.stdin.read().strip().split('\n')
# 	lines = '''3 5
# -2 -3
# -1 2
# -1 3
# -3 2
# -2 1'''.strip().split('\n')
# 	lines = '''1 2
# 1 1
# -1 -1'''.split('\n')

	global scc_id

	clause_count, vertex_count, graph = read_inputs(lines)
	sccs = [[] for _ in range(vertex_count * 2)]
	for v in graph:
		if not v.reverse_visited:
			v.explore()
	
	for v in sorted(graph, key=lambda v: - v.post_order):
		if not v.visited:
			v.explore(r=False, sccs=sccs)
			scc_id += 1

	for i in range(0, len(graph), 2):
		if graph[i].scc == graph[i + 1].scc:
			print('UNSATISFIABLE')
			return

	metagraph = [MetaVertex(i, sccs[i]) for i in range(scc_id)]	
	for v in metagraph:
		for u in v.vertices:
			for w in u.reachables:
				if w.scc != v.scc:
					v.reachables.add(w)

	for v in metagraph:
		if not v.visited:
			v.explore()
	
	for scc in sorted(metagraph, key=lambda x: x.post):
		for v in sorted(scc.vertices, key=lambda x: - x.post_order):
			if v.val == None:
				_, position = get_pos(v.key)
				v.val = 1
				graph[position].val = 0

	print('SATISFIABLE')
	output = []
	for v in graph[::2]:
		sign = 1 if v.val == 1 else -1
		output.append(sign * v.key)
	print(*output)


if __name__ == '__main__':
	threading.Thread(target=is_satisfiable).start()


