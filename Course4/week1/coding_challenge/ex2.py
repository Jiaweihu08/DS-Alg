#python3

class Node:
	def __init__(self, symbol, prev, id):
		self.symbol = symbol
		self.prev = prev
		self.id = id
		self.reachables = []

	def is_leaf(self):
		return not bool(self.reachables)

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
				symbol = next(text, 'stop')
				if symbol == 'stop':
				 	return index if w.is_leaf() else None
				v = w
				break
			elif i == len(v.reachables):
				return

def trie_matching(text, trie):
	index = 0
	while text:
		pos = preffix_trie_matching(text, trie, index)
		if pos != None:
			print(pos, end=' ')
		text = text[1:]
		index += 1


def main():
# 	lines = '''AAA
# 1
# AA'''.split('\n')
# 	text = lines[0]
# 	n = int(lines[1])
# 	patterns = lines[2:]

	text = input()
	n = int(input())
	patterns = [input() for _ in range(n)]


	trie = trie_construction(patterns)
	trie_matching(text, trie)
	print()


if __name__ == '__main__':
	main()