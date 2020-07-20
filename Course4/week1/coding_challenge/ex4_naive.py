#python3


def trie_construction(text):
	root = {'s': 0, 'l': 0, 'adj': [], 'i': None}
	n = len(text)
	for i in range(n):
		cur_node = root
		for j in range(i, n):
			add_new = True
			for node in cur_node['adj']:
				if text[node['s']] == text[j]:
					cur_node = node
					add_new = False
					break
			if add_new:
				index = i if j == n - 1 else None
				new_node = {'s':j, 'l':1, 'adj':[], 'i': index}
				cur_node['adj'].append(new_node)
				cur_node = new_node
	return root

def trie_compression(trie):
	n = len(trie['adj'])
	if n == 0:
		return trie
	elif n == 1:
		w = trie['adj'][0]
		trie['adj'] = w['adj']
		trie['i'] = w['i']
		trie['l'] += 1
		trie_compression(trie)
	else:
		for w in trie['adj']:
			w = trie_compression(w)
	return trie

def pre_order_traversal(root, text):
	if root['adj'] == []:
		return
	for node in root['adj']:
		print(text[node['s']:node['s'] + node['l']])
		pre_order_traversal(node, text)

def main():
	text = input()
	# text = 'GGGCTCAGCCAGG$'
	trie = trie_construction(text)
	tree = trie_compression(trie)
	pre_order_traversal(tree, text)

	

if __name__ == '__main__':
	main()

