#python3
from itertools import product

class EnergyInf:
	def __init__(self):
		self.n = int(input())
		self.A = [list(map(float, input().split())) for _ in range(self.n)]
		self.pivot_col, self.pivot_row = 0, 0
		self.result = [0] * self.n

	# def __init__(self, lines):
	# 	self.n = int(lines[0])
	# 	self.A = [list(map(float, line.split())) for line in lines[1:]]
	# 	self.pivot_row = 0
	# 	self.pivot_col = 0
	# 	self.result = [0] * self.n

	def swap_rows(self):
		# print('swapping rows:', self.pivot_row, self.pivot_col)
		if self.A[self.pivot_row][self.pivot_col] == 0:
			row_range = range(self.pivot_row, self.n)
			col_range = range(self.pivot_col, self.n)
			for i, j in product(row_range, col_range):
				# print(j, i)
				if self.A[j][i] != 0:
					self.A[self.pivot_row], self.A[j] = self.A[j], self.A[self.pivot_row]
					# print('break')
					# print(self.A)
					self.pivot_col = i
					break

	def gaussian_elimination(self):
		while self.pivot_col < self.n and self.pivot_row < self.n:
			self.swap_rows()
			row = self.A[self.pivot_row]
			if row[self.pivot_col] != 1:
				factor = row[self.pivot_col]
				for i in range(self.pivot_col, self.n + 1):
					row[i] /= factor

			for row_ in self.A[self.pivot_row + 1:]:
				if row_[self.pivot_col] == 0:
					continue
				factor = -row_[self.pivot_col]
				for i in range(self.pivot_col, self.n + 1):
					row_[i] += factor * row[i]
			# print(self.A)
			self.pivot_row += 1
			self.pivot_col += 1

	def solve_eqs(self):
		if not self.result:
			return
		
		self.gaussian_elimination()
		# print(self.A)
		
		self.result[-1] = self.A[-1][-1] / self.A[-1][-2]
		for i in reversed(range(self.n - 1)):
			sum_ = sum([self.A[i][j] * self.result[j] for j in range(i + 1, self.n)])
			self.result[i] = (self.A[i][-1] - sum_) / self.A[i][i]
		
		for val in self.result:
			print('{:.6f}'.format(val), end=' ')

if __name__ == '__main__':
# 	lines = '''4
# 0 0 1 0 2
# 1 0 0 0 0
# 0 0 0 1 1
# 0 1 0 0 6'''.split('\n')
# 	energy_solver = EnergyInf(lines)

	energy_solver = EnergyInf()
	energy_solver.solve_eqs()
	




