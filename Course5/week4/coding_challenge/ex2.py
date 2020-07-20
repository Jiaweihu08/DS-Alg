#python3

import sys
import threading

sys.setrecursionlimit(10**6)
threading.stack_size(2**26)

class Vertex:
	def __init__(self, factor):
		self.factor = factor
		self.best_factor = None
		self.children = []

def read_tree():
	lines = sys.stdin.read().strip().split('\n')
# 	lines = '''5
# 1 5 3 7 5
# 5 4
# 2 3
# 4 2
# 1 2'''.split('\n')
	tree = [Vertex(factor) for factor in map(int, lines[1].split())]
	for line in lines[2:]:
		c, p = map(int, line.split())
		tree[p - 1].children.append(c - 1)
		tree[c - 1].children.append(p - 1)
	return tree

def dfs(tree, vertex, parent):
	# print('v:{}, p:{}'.format(vertex + 1, parent + 1))
	node = tree[vertex]
	if node.best_factor == None:
		if len(node.children) == 1 and node.children[0] == parent:
			node.best_factor = node.factor
		else:
			m1 = node.factor
			m2 = 0
			for child in node.children:
				if child != parent:
					m2 += dfs(tree, child, vertex)
					for grand_child in tree[child].children:
						if grand_child != vertex:
							m1 += dfs(tree, grand_child, child)
			# m2 = 0
			# for child in node.children:
			# 	if child != parent:
			# 		m2 += dfs(tree, child, vertex)
			node.best_factor = max(m1, m2)
	return node.best_factor

def max_factor_indep_tree_subset(tree):
	size = len(tree)
	if size == 0:
		return 0
	return dfs(tree, 0, -1)

def main():
	tree = read_tree()
	best_factor = max_factor_indep_tree_subset(tree)
	print(best_factor)


threading.Thread(target=main).start()



