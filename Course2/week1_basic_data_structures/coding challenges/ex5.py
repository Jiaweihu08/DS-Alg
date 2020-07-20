# from time import process_time


class Stack:
	def __init__(self):
		self.values = []
		self.max = []

	def __repr__(self):
		return str(self.values)

	def Push(self, v):
		self.values.append(v)
		if self.max == []:
			# print('max empty, adding:',v)
			self.max.append(v)
		elif v >= self.max[-1]:
			self.max.append(v)
			# print('max not empty, just added a new v', v)
			# print(self.max)

	def Pop(self):
		v = self.values.pop(-1)
		if v == self.max[-1]:
			self.max.pop(-1)
		return v

	def Max(self):
		if self.max:
			return self.max[-1]
		return

	def IsEmpty(self):
		return not bool(self.values)


class Queue:
	def __init__(self, ):
		self.s1 = Stack()
		self.s2 = Stack()

	def enQueue(self,x):
		self.s1.Push(x)

	def deQueue(self):
		if self.s1.IsEmpty() and self.s2.IsEmpty():
			print('The queue is empty!')
			return
		elif self.s2.IsEmpty():
			while not self.s1.IsEmpty():
				self.s2.Push(self.s1.Pop())
		return self.s2.Pop()

	def Max(self):
		if self.s1.max and self.s2.max:
			return max(self.s1.Max(), self.s2.Max())
		elif self.s1.max:
			return self.s1.Max()
		else:
			return self.s2.Max()

def main():
	n = int(input())
	sequence = list(map(int, input().split()))
	m = int(input())

	# sequence = list(map(int, '6 5 4 3 2 1'.split()))
	# m = 2
	# print(sequence[:m])
	

	# n = 100000
	# sequence = [0] * n
	# m = 33333

	# start = process_time()

	q = Queue()
	for num in sequence[:m]:
		q.enQueue(num)

	windows_max = [q.Max()]
	for num in sequence[m:]:
		q.deQueue()
		q.enQueue(num)
		windows_max.append(q.Max())
	print(*windows_max)

	# print(process_time() - start)
if __name__ == '__main__':
	main()