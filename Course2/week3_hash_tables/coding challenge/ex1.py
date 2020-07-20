class PhoneBook:
	def __init__(self):
		self.book = [None] * 10 ** 7

	def add(self, number, name):
		self.book[number] = name

	def delete(self, number):
		self.book[number] = None

	def find(self, number):
		if self.book[number]:
			return self.book[number]
		return 'not found'


def main():
	book = PhoneBook()
	for _ in range(int(input())):
		op = input().split()
		if op[0] == 'add':
			book.add(int(op[1]), op[2])
		elif op[0] == 'find':
			print(book.find(int(op[1])))
		else:
			book.delete(int(op[1]))


if __name__ == '__main__':
	main()