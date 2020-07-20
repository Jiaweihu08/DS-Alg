import sys


class Solver:
	def __init__(self, s, t):
		self.s = s
		self.t = t
		self.m1 = 10 ** 9 + 5
		self.m2 = 10 ** 9 + 11
		self.x = 80
		self.l = min(len(s), len(t))
		self.y_mod1, self.y_mod2 = self.get_pow_x()
		self.s_hash_table_mod1, self.s_hash_table_mod2 = self.get_hash_table()
		self.t_hash_mod1, self.t_hash_mod2 = self.get_hashes(self.t)

	def get_pow_x(self):
		l = self.l + 1
		pow_x_mod1 = [1] * l
		pow_x_mod2 = [1] * l
		for i in range(1, l):
			pow_x_mod1[i] = self.x * pow_x_mod1[i - 1] % self.m1
			pow_x_mod2[i] = self.x * pow_x_mod2[i - 1] % self.m2
		
		return pow_x_mod1, pow_x_mod2

	def get_hashes(self, s):
		n = len(s) + 1
		h_mod1 = [0] * n
		h_mod2 = [0] * n
		for i in range(1, n):
			h_mod1[i] = (self.x * h_mod1[i - 1] + ord(s[i - 1])) % self.m1
			h_mod2[i] = (self.x * h_mod2[i - 1] + ord(s[i - 1])) % self.m2
		return h_mod1, h_mod2

	def get_hash_table(self):
		h_mod1, h_mod2 = self.get_hashes(self.s)
		# print(h_mod1)
		n = len(self.s) + 1
		s_hashes_mod1 = [[] for _ in range(n - 1)]
		s_hashes_mod2 = [[] for _ in range(n - 1)]
		for k in range(1, self.l + 1):
			y_mod1 = self.y_mod1[k]
			y_mod2 = self.y_mod2[k]

			for i in range(n - k):
				mod_1 = (h_mod1[i + k] - y_mod1 * h_mod1[i]) % self.m1
				mod_2 = (h_mod2[i + k] - y_mod2 * h_mod2[i]) % self.m2
				s_hashes_mod1[k - 1].append(mod_1)
				s_hashes_mod2[k - 1].append(mod_2)

		return s_hashes_mod1, s_hashes_mod2

	def solve(self):
		low = 1
		high = self.l
		idx_s = idx_t = length = 0
		while low < high:
			k = (low + high + 1) // 2
			y_mod1 = self.y_mod1[k]
			y_mod2 = self.y_mod2[k]
			stop = False
			for i in range(len(self.t) - k + 1):
				t_mod1 = (self.t_hash_mod1[i + k] - y_mod1 * \
										self.t_hash_mod1[i]) % self.m1
				t_mod2 = (self.t_hash_mod2[i + k] - y_mod2 * \
										self.t_hash_mod2[i]) % self.m2

				for j in range(len(self.s_hash_table_mod1[k - 1])):
					s_mod1 = self.s_hash_table_mod1[k - 1][j]
					s_mod2 = self.s_hash_table_mod2[k - 1][j]
					if t_mod1 == s_mod1 and t_mod2 == s_mod2:
						# print(t_mod1, s_mod1, t_mod2, s_mod2)
						# print(self.s[j:j+k], self.t[i:i+k])
						idx_s, idx_t, length = j, i, k
						stop = True
						break
				if stop:
					low = k
					break

			if not stop:
				high = k - 1
		return idx_s, idx_t, length


def main():
	lines = ['cool toolbox', 'aaa bb', 'aabaa babbaab']
	for line in lines:
	# for line in sys.stdin.readlines():
		solver = Solver(*line.split())
		print(solver.s_hash_table_mod1)
		print(*solver.solve())


if __name__ == '__main__':
	main()



