#python3

class Node:
	def __init__(self, symbol, prev, id_):
		self.symbol = symbol
		self.prev = prev
		self.id = id_
		self.reachables = []
		self.spell = False

	def is_leaf(self):
		return not bool(self.reachables)

	def __repr__(self):
		return '{}->{}:{}, spell:{}\n'.format(self.prev, self.id,
											self.symbol, self.spell)
def trie_construction(patterns):
	root = Node('root', 0, 0)
	id_ = 1
	for pattern in patterns:
		cur_node = root
		n = len(pattern)
		for i in range(n):
			if cur_node.spell:
				break
			cur_symbol = pattern[i]
			add_new = True
			for node in cur_node.reachables:
				if node.symbol == cur_symbol:
					cur_node = node
					if i == n - 1:
						cur_node.spell = True
					add_new = False
					break
			if add_new:
				node = Node(cur_symbol, cur_node.id, id_)
				cur_node.reachables.append(node)
				cur_node = node
				id_ += 1
				if i == n - 1:
					cur_node.spell = True

	return root

def preffix_trie_matching(text, trie, index):
	text = iter(text)
	symbol = next(text)
	v = trie

	while True:
		if v.is_leaf():
			return index
		
		i = 0
		for w in v.reachables:
			i += 1
			if w.symbol == symbol:
				if w.spell:
					return index

				symbol = next(text, 'stop')
				if symbol == 'stop':
				 	return index if (w.is_leaf() or w.spell) else None
				
				v = w
				break

			elif i == len(v.reachables):
				return

def trie_matching(text, trie):
	# indices = set()
	index = 0
	while text:
		pos = preffix_trie_matching(text, trie, index)
		if pos != None:
			# indices.add(pos)
			print(pos, end=' ')
		text = text[1:]
		index += 1
	# return sorted(indices)

# def pre_order_traversal(trie):
# 	if trie.is_leaf():
# 		return
# 	for node in trie.reachables:
# 		print(node)
# 		pre_order_traversal(node)

def main():
# 	lines = '''AATCGGGTTCAATCGGGGT
# 2
# ATCG
# GGGT'''.split('\n')
# 	text = lines[0]
# 	n = int(lines[1])
# 	patterns = lines[2:]

	text = input()
	n = int(input())
	patterns = [input() for _ in range(n)]


	trie = trie_construction(patterns)
	# pre_order_traversal(trie)
	trie_matching(text, trie)


if __name__ == '__main__':
	main()