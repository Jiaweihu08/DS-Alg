# from random import randint

def precompute_hashes(S, m1, m2, x):
	n = len(S) + 1
	h_mod1, h_mod2 = [0] * n, [0] * n
	pow_x_mod1 = [1] * n
	pow_x_mod2 = [1] * n

	for i in range(1, n):
		h_mod1[i] = (x * h_mod1[i - 1] + ord(S[i - 1])) % m1
		h_mod2[i] = (x * h_mod2[i - 1] + ord(S[i - 1])) % m2

		pow_x_mod1[i] = x * pow_x_mod1[i - 1] % m1
		pow_x_mod2[i] = x * pow_x_mod2[i - 1] % m2

	return h_mod1, h_mod2, pow_x_mod1, pow_x_mod2

class Solver:
	def __init__(self, S):
		self.s = S
		self.m1 = 10 ** 9 + 7
		self.m2 = 10 ** 9 + 9
		self.x = 99 #randint(1, self.m1)
		self.h_mod1, self.h_mod2,\
		self.pow_x_mod1, self.pow_x_mod2 = precompute_hashes(S,
															self.m1,
															self.m2,
															self.x)
	
	def solve(self, a, b, l):

		y_mod1 = self.pow_x_mod1[l]
		y_mod2 = self.pow_x_mod2[l]

		ha_mod1 = (self.h_mod1[a + l] - y_mod1 * self.h_mod1[a]) % self.m1
		ha_mod2 = (self.h_mod2[a + l] - y_mod2 * self.h_mod2[a]) % self.m2

		hb_mod1 = (self.h_mod1[b + l] - y_mod1 * self.h_mod1[b]) % self.m1
		hb_mod2 = (self.h_mod2[b + l] - y_mod2 * self.h_mod2[b]) % self.m2

		if ha_mod1 == hb_mod1 and ha_mod2 == hb_mod2:
			print('Yes')
		else:
			print('No')

def main():
	S = input()
	solver = Solver(S)
	for _ in range(int(input())):
		a, b, l = list(map(int, input().split()))
		solver.solve(a, b, l)

	# S = 'trololo'
	# solver = Solver(S)
	# for a, b, l in [(0, 0, 7), (2, 4, 3), (3, 5, 1), (1, 3, 2)]:
	# 	print(a, b, l)
	# 	solver.solve(a, b, l)



if __name__ == '__main__':
	main()



