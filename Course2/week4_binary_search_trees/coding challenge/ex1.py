import sys, threading
from collections import namedtuple

Node = namedtuple('Node', ['key', 'left', 'right'])

class TreeWalker:
	def __init__(self, nodes):
		self.nodes = nodes

	def in_order_traversal(self, node):
		if node.left != -1:
			self.in_order_traversal(self.nodes[node.left])
		print(node.key, end=' ')
		if node.right != -1:
			self.in_order_traversal(self.nodes[node.right])

	def pre_order_traversal(self, node):
		print(node.key, end=' ')
		if node.left != -1:
			self.pre_order_traversal(self.nodes[node.left])
		if node.right != -1:
			self.pre_order_traversal(self.nodes[node.right])

	def post_order_traversal(self, node):
		if node.left != -1:
			self.post_order_traversal(self.nodes[node.left])
		if node.right != -1:
			self.post_order_traversal(self.nodes[node.right])
		print(node.key, end=' ')

def main():
	nodes = [Node(*map(int, input().split())) for _ in range(int(input()))]
	# nodes = [Node(4,1,2), Node(2,3,4), Node(5,-1,-1), Node(1,-1,-1), Node(3,-1,-1)]
	# nodes_ = ['0 7 2',
	# 		'10 -1 -1',
	# 		'20 -1 6',
	# 		'30 8 9',
	# 		'40 3 -1',
	# 		'50 -1 -1',
	# 		'60 1 -1',
	# 		'70 5 4',
	# 		'80 -1 -1',
	# 		'90 -1 -1']
	# nodes = [Node(*map(int, node.split())) for node in nodes_]
	walker = TreeWalker(nodes)
	walker.in_order_traversal(nodes[0])
	print()
	walker.pre_order_traversal(nodes[0])
	print()
	walker.post_order_traversal(nodes[0])
	print()


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
