#python3

class Node:
	def __init__(self, symbol, prev, id):
		self.symbol = symbol
		self.prev = prev
		self.id = id
		self.reachables = []

	def __repr__(self):
		return "{}->{}:{}".format(self.prev, self.id, self.symbol)

def trie_construction(patterns):
	root = Node('root', 0, 0)
	id_ = 1
	for pattern in patterns:
		cur_node = root
		for i in range(len(pattern)):
			cur_symbol = pattern[i]
			add_new = True
			for node in cur_node.reachables:
				if node.symbol == cur_symbol:
					cur_node = node
					add_new = False
					break
			if add_new:
				node = Node(cur_symbol, cur_node.id, id_)
				cur_node.reachables.append(node)
				cur_node = node
				id_ += 1

	return root

def pre_order_traversal(trie):
	if not trie.reachables:
		return
	for node in trie.reachables:
		print(node)
		pre_order_traversal(node)

def main():
# 	lines = '''1
# ATA'''.split('\n')
# 	n = int(lines[0])
# 	patterns = lines[1:]

	n = int(input())
	patterns = [input() for _ in range(n)]

	Trie = trie_construction(patterns)
	pre_order_traversal(Trie)



if __name__ == '__main__':
	main()