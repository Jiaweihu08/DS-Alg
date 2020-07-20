#python3

import sys
sys.setrecursionlimit(200000)


def get_suffix_tree(text):
	n = len(text)
	root = {'s':None, 'l':None, 'adj':[]}
	for i in range(n):
		cur_node = root
		j = i
		while j < n:
			# print('i, j:', i, j)
			add_new = True
			for node in cur_node['adj']:
				start, length = node['s'], node['l']
				if text[start] != text[j]:
					continue
				if length == 1:
					# print('start:', start, text[start])
					# print('length == 1, jumping to its child nodes')
					cur_node = node
					j += 1
				elif text[start:start + length] == text[j:j + length]:
					# print('len > 1, node text == part of the pattern')
					# print(text[start:start + length])
					cur_node = node
					j += length
				else:
					# print(cur_node, node)
					k = 1
					while text[start + k] == text[j + k]:
						k += 1
					# print('else case')
					# print('k:', k)
					# print('original node text:', text[start:start+length])
					# print('node text after splitting:', text[start:start+k])
					# print('node text that became a child:', text[start+k:start+length])
					# print('text of the new node:', text[j+k:n])
					split_node = {'s': start + k, 'l': length - k, 'adj': node['adj']}
					new_node = {'s': j + k, 'l': n - j - k, 'adj': []}
					node['l'], node['adj'] = k, []
					node['adj'].append(split_node)
					node['adj'].append(new_node)
					j = n

				# print()
				add_new = False
				break
			if add_new:
				# print('start, length:', j, n-j)
				# print('adding a new node, text:{}\n'.format(text[j:n]))
				new_node = {'s':j, 'l':n - j, 'adj':[]}
				cur_node['adj'].append(new_node)
				j = n
	
	pre_order_traversal(root, text)

def pre_order_traversal(root, text):
	if root['adj'] == []:
		return
	for node in root['adj']:
		print(text[node['s']:node['s'] + node['l']])
		pre_order_traversal(node, text)


if __name__ == '__main__':
	# text = 'A'*5000+'$'
	text1 = 'CCAAGCT'
	text2 = 'CATGCTG'
	text = text1 + '#' + text2 + '$'
	get_suffix_tree(text)









