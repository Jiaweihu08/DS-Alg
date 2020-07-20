#python3

import sys
import threading
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)



def get_suffix_tree(text, pos):
	n = len(text)
	root = {'s':0, 'l':0, 'adj':[]}
	for i in range(n):
		cur_node = root
		j = i
		while j < n:
			add_new = True
			for node in cur_node['adj']:
				start, length = node['s'], node['l']
				if text[start] != text[j]:
					continue
				if length == 1:
					cur_node = node
					j += 1
				elif text[start:start + length] == text[j:j + length]:
					cur_node = node
					j += length
				else:
					k = 1
					while text[start + k] == text[j + k]:
						k += 1

					split_node = {'s': start + k, 'l': length - k, 'adj': node['adj']}
					new_node = {'s': j + k, 'l': n - j - k, 'adj': []}

					node['l'], node['adj'] = k, []
					node['adj'].append(split_node)
					node['adj'].append(new_node)
					j = n
				add_new = False
				break
			
			if add_new:
				new_node = {'s':j, 'l':n - j, 'adj':[]}
				cur_node['adj'].append(new_node)
				j = n
	
	mark_l_leaves(root, pos)
	return root

def mark_l_leaves(root, pos):
	if root['adj'] == []:
		if root['s'] <= pos:
			root['is_l'] = True
			return True
		root['is_l'] = False
		return False
	
	l_leaves = [mark_l_leaves(node, pos) for node in root['adj']]
	root['is_l'] = all(l_leaves)
	return root['is_l']

def dfs_traversal(root, text, pos):
	if root['adj'] == []:
		return

	for node in root['adj']:
		print(text[node['s']:node['s'] + node['l']],
				'---->', node['is_l'])
		dfs_traversal(node, text, pos)

def dfs(root, text, pos):
	start, end = root['s'], root['s'] + root['l']
	child_nodes = root['adj']

	c_node = 'root' if end == 0 else text[start:end]

	if child_nodes == []:
		return (text[start], True) if start < pos else (None, False)
	
	if root['is_l']:
		return text[start], True
	
	max_len = float('inf')
	cur_text = text[start:end]
	text_to_add = ''

	for node in child_nodes:

		# print('Parent node:{}, current node:{}'.format(
		# 	c_node,
		# 	text[node['s']:node['s']+node['l']]))

		new_text, is_l_branch = dfs(node, text, pos)
		if is_l_branch:
			text_len = len(new_text)
			if text_len < max_len:
				max_len = text_len
				text_to_add = new_text
				no_change = False
	
	# print(c_node, '|', text_to_add)
	if text_to_add == '':
		return None, False
	return cur_text + text_to_add, True

if __name__ == '__main__':
	text1, text2 = input(), input()
	text = text1 + '#' + text2 + '$'
	pos = len(text1)

	# text1 = 'ATGCGATGACCTGACTGA'
	# text2 = 'CTCAACGTATTGGCCAGA'
	# text = text1 + '#' + text2 + '$'
	# pos = len(text1)
	
	root = get_suffix_tree(text, pos)
	# dfs_traversal(root, text, pos)
	print(dfs(root, text, pos)[0])



