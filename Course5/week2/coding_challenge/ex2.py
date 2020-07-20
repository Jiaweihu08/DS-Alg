#python3
from itertools import combinations, product
import numpy as np

class GaussianSolver:
	def __init__(self, A, indices):
		self.eqs = A[indices, :]
		self.pivot_row, self.pivot_col = 0, 0
		self.n = len(indices)
		self.result = [0] * self.n
		# self.indices = indices

	def swap_rows(self):
		if self.eqs[self.pivot_row, self.pivot_col] == 0:
			row_range = range(self.pivot_row, self.n)
			col_range = range(self.pivot_col, self.n)
			for i, j in product(row_range, col_range):
				if self.eqs[j, i] != 0.:
					self.eqs[[self.pivot_row, j]] = self.eqs[[j, self.pivot_row]]
					self.pivot_col = i
					break

	def gaussian_elimination(self):
		while self.pivot_row < self.n and self.pivot_col < self.n:
			self.swap_rows()

			row = self.eqs[self.pivot_row, :]
			pivot_val = row[self.pivot_col]
			
			if pivot_val == 0:
				return
			if pivot_val != 1:
				row /= pivot_val

			for row_ in self.eqs[self.pivot_row + 1:, :]:
				if row_[self.pivot_col] == 0:
					continue
				factor = -row_[self.pivot_col]

				row_[self.pivot_col:] += factor * row[self.pivot_col:]
			# if self.indices == (0, 1):
			# 	print(self.eqs)
			self.pivot_row += 1
			self.pivot_col += 1		

	def solve_eqs(self):
		if not self.result:
			return []

		self.gaussian_elimination()

		if self.eqs[-1, -2] == 0:
			return []
		else:
			last_val = self.eqs[-1, -1] / self.eqs[-1, -2]
			if last_val < 0:
				return []
			self.result[-1] = last_val
		for i in reversed(range(self.n - 1)):
			sum_ = sum(self.eqs[i, i + 1:-1] * np.array(self.result[i + 1:]))
			self.result[i] = (self.eqs[i, -1] - sum_) / self.eqs[i, i]
		return self.result


class Diet:
	def __init__(self):
		self.n, self.m = map(int, input().split())
		self.A = [list(map(float, input().split())) for _ in range(self.n)]
		self.b = list(map(float, input().split()))
		for i in range(self.n):
			self.A[i].append(self.b[i])
		self.get_additional_constraints()
		self.pleasures = list(map(float, input().split()))
		self.candidates = []

	# def __init__(self, lines):
	# 	self.n, self.m = map(int, lines[0].split())
	# 	self.A = [list(map(float, line.split())) for line in lines[1:-2]]
	# 	b = list(map(float, lines[-2].split()))
	# 	for i in range(self.n):
	# 		self.A[i].append(b[i])
	# 	self.get_additional_constraints()
	# 	self.pleasures = list(map(float, lines[-1].split()))
	# 	self.candidates = []

	def get_additional_constraints(self):
		infinity_constrain = [1] * (self.m + 1)
		infinity_constrain[-1] = 10 ** 9
		self.A.append(infinity_constrain)
		
		for j in range(self.m):
			constraint = [0] * (self.m + 1)
			constraint[j] = 1
			self.A.append(constraint)
		
		self.A = np.array(self.A)


	def is_candidate(self, result, indices):
		result = np.array(result)
		for i in range(self.n + self.m + 1):
			if i in indices:
				continue
			row = self.A[i]
			sum_ = sum(result * row[:-1])
			condition = sum_ > row[-1] if i <= self.n else sum_ < row[-1]
			if  condition:
				return False
		return True

	def solve(self):
		for indices in combinations(range(self.n + self.m + 1), self.m):
			result = GaussianSolver(self.A, indices).solve_eqs()
			if result != []:
				if self.is_candidate(result, indices):
					is_inf = 1 if self.n in indices else 0
					self.candidates.append((result, is_inf))

	def vertex_value(self, index):
		return sum(self.pleasures * self.candidates[index][0])

	def get_best_vertex_values(self):
		# for cand in self.candidates:
		# 	print(cand)
		if self.candidates == []:
			print('No solution')
			return
		self.pleasures = np.array(self.pleasures)
		best_value = float('-inf')
		best_index = None
		for i in range(len(self.candidates)):
			vertex_val = self.vertex_value(i)
			if vertex_val >= best_value:
				best_value = vertex_val
				best_index = i

		if self.candidates[best_index][1]:
			print('Infinity')
			return

		print('Bounded solution')
		for amount in self.candidates[best_index][0]:
			print('{:.15f}'.format(amount), end=' ')
		return


if __name__ == '__main__':
# 	lines = '''4 4
# 68 -16 87 -11
# -86 32 33 -46
# -67 -36 9 16
# 2 53 -90 38
# 15272 32777 6863 5483
# 82 -55 -20 93'''.split('\n')
	# best_diet = Diet(lines)
	# print(best_diet.A)
	best_diet = Diet()
	best_diet.solve()
	best_diet.get_best_vertex_values()





