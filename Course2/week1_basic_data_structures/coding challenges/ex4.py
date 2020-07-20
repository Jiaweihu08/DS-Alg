class Stack:
	def __init__(self):
		self.stack_ = []
		self.max = []

	def Push(self, v):
		self.stack_.append(v)
		if self.max:
			if v >= self.max[-1]:
				self.max.append(v)
		else:
			self.max.append(v)

	def Pop(self):
		v = self.stack_.pop(-1)
		if v == self.max[-1]:
			m = self.max.pop(-1)

	def Max(self):
		return self.max[-1]

def main():
	stack = Stack()
	ops = [input().split() for _ in range(int(input()))]
	for op in ops:
		if op[0] == 'max':
			print(stack.Max())
		elif op[0] == 'pop':
			stack.Pop()
		else:
			stack.Push(int(op[1]))

if __name__ == '__main__':
	main()