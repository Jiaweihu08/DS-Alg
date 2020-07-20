class Query:
	def __init__(self, op, s):
		self.op = op
		if op == 'check':
			self.pos = int(s)
		else:
			self.s = s


class PhoneBook:
	def __init__(self, m):
		self.book = [[]] * m
		self.m = m

	def poly_hash(self, s, p=1000000007, x=263):
		h = 0
		for i in reversed(range(len(s))):
			h = (h * x + ord(s[i])) % p
		return h % self.m

	def add(self, s):
		pos = self.poly_hash(s)
		if self.book[pos]:
			for name in self.book[pos]:
				if name == s:
					return
			self.book[pos] = [s] + self.book[pos]
		else:
			self.book[pos] = [s] + self.book[pos]

	def delete(self, s):
		pos = self.poly_hash(s)
		for name in self.book[pos]:
			if name == s:
				self.book[pos].remove(name)

	def find(self, s):
		pos = self.poly_hash(s)
		for name in self.book[pos]:
			if name == s:
				print('yes')
				return
		print('no')

	def check(self, i):
		print(*self.book[i])

def main():
	book = PhoneBook(int(input()))
	for _ in range(int(input())):
		query = Query(*input().split())
		if query.op == 'add':
			book.add(query.s)
		elif query.op == 'del':
			book.delete(query.s)
		elif query.op == 'find':
			book.find(query.s)
		else:
			book.check(query.pos)
	
	# book = PhoneBook(5)
	# queries = ['add world', 'add HellO', 'check 4', 'del HellO', 'check 4']
	# for q in queries:
	# 	query = Query(*q.split())
	# 	if query.op == 'add':
	# 		book.add(query.s)
	# 	elif query.op == 'del':
	# 		book.delete(query.s)
	# 	elif query.op == 'find':
	# 		book.find(query.s)
	# 	else:
	# 		book.check(query.pos)
	# 	print(book.book)
	# print(poly_hash('HellO'))

# def poly_hash(s, m=5, p=1000000007, x=263):
# 		h = 0
# 		for i in reversed(range(len(s))):
# 			h = (h * x + ord(s[i])) % p
# 		return h % m


if __name__ == '__main__':
	main()
	