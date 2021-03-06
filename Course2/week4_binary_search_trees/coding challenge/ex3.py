import sys, threading


def is_valid_tree(node, tree, max_=float('inf'), min_=float('-inf')):
	is_bst = True
	if node[1] != -1:
		left = tree[node[1]]
		if left[0] >= node[0] or left[0] < min_:
			# print(node)
			# print('going left, node:{}, node.left:{}'.format(node[0], tree[node[1]][0]))
			return False
		is_bst = is_valid_tree(left, tree, node[0], min_)
		# print(node, 'left', is_bst)

	if node[2] != -1 and is_bst:
		right = tree[node[2]]
		if right[0] < node[0] or right[0] > max_:
			return False
		is_bst = is_valid_tree(right, tree, max_, node[0])
		# print(node, 'right', is_bst)
	return is_bst


def main():
	# nodes_ = '''4 1 2
	# 			2 3 4
	# 			6 5 6
	# 			1 -1 -1
	# 			3 -1 -1
	# 			4 7 -1
	# 			7 -1 -1
	# 			5 8 9
	# 			5 -1 -1
	# 			5 -1 -1'''.split('\n')
	# tree = [tuple(map(int, node.split())) for node in nodes_]

	n = int(input())
	if n == 0:
		print('CORRECT')
		return

	tree = [tuple(map(int, input().split())) for _ in range(n)]

	if len(tree) == 1:
		print('CORRECT')
		return

	is_bst = is_valid_tree(tree[0], tree)
	# print(is_bst)
	if is_bst:
		print('CORRECT')
	else:
		print('INCORRECT')


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()