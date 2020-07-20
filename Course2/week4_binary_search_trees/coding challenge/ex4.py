# class Node:
# 	def __init__(self, key, parent=None, left=None, right=None):
# 		self.key = key
# 		self.parent = parent
# 		self.left = left
# 		self.right = right

# class BST:
# 	def __init__(self):
# 		self.m = 10**9 + 1
# 		self.x = 0
# 		self.root = Node()

# 	def add(self, i):
# 		num = (i + self.x) % self.m
# 		P = self.find(i)
# 		#add a new node as a child node of P
# 		pass

# 	def delete(self, i):
# 		num = (i + self.x) % self.m
# 		N = self.find(i)
# 		if N.right == None:
# 			#remove N, promote left
# 		else:
# 			X = self.next(N)
# 			#replace N by X, promote X.right

# 	def find(self, i, R = self.root):
# 		num = (i + self.x) % self.m
# 		if R.key == num:
# 			return R
# 		elif R.key > num:
# 			if R.left != None:
# 				return self.find(i, R.left)
# 			return R
# 		else:
# 			if R.right != None:
# 				return self.find(i, R.right)
# 			return R

# 	def next(N):
# 		if N.right != None:
# 			return self.left_descendent(N.right)
# 		return self.right_ancestor(N)

# 	def left_descendent(N):
# 		if N.left == None:
# 			return N
# 		return self.left_descendent(N.left)

# 	def right_ancestor(N):
# 		if N.key < N.parent.key:
# 			return N.parent
# 		return right_ancestor(N.parent)
		

# 	def sum(self, l, r):
# 		l = (l + self.x) % self.m
# 		r = (r + self.x) % self.m
# 		N = self.find(l)
# 		while N.key <= r:
# 			if N.key >= x:
# 				self.x += N.key
# 			N = self.next(N)

# 		return self.x


# def main():
# 	tree = BST()
# 	for _ in range(int(input()):
# 		op = input().split()
# 		if len(op) == 3:
# 			tree.sum(int(op[1]), int(op[2])))
# 		elif op[0] == '+':
# 			tree.add(int(op[1]))
# 		elif op[0] == '-':
# 			tree.delete(int(op[1]))
# 		else:
# 			tree.find(int(op[1]))