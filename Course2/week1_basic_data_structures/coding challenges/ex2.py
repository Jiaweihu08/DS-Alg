import sys
import threading


class Node:
    def __init__(self, label):
        self.label = label
        self.children = []

    def add_child(self, node):
        self.children.append(node)
    
    def __repr__(self):
        name = 'tree' if self.label == -1 else 'node_({})'.format(self.label)
        return name

def get_height(tree):
    if not tree.children:
        return 1
    return 1 + max(get_height(child) for child in tree.children)

def compute_tree_and_get_height(parents):
    nodes = [Node(p) for p in parents]

    for child_index in range(len(parents)):
        parent_index = parents[child_index]
        if parent_index == -1:
            root = child_index
        else:
            nodes[parent_index].add_child(nodes[child_index])

    height = get_height(nodes[root])
    
    return height


# if __name__ == '__main__':
# 	n = input()
# 	# parents = list(map(int, input().split()))
# 	# parents = list(map(int, '-1 0 4 0 3'.split()))
	# parents = list(map(int, '4 -1 4 1 1'.split()))
	# # parents = [-1]
	# height = compute_tree_and_get_height(parents)
	# print(height)


def main():
	n = input()
	parents = list(map(int, input().split()))
	print(compute_tree_and_get_height(parents))

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
