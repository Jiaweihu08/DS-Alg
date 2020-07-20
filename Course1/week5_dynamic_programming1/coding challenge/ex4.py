def common_seq(A, B):
	n = len(A)
	m = len(B)
	D = [[m] + [i for i in range(1, n + 1)] for m in range(m + 1)]

	for j in range(1, m + 1):
		for i in range(1, n + 1):
			insertion = D[j][i-1] + 1
			deletion = D[j-1][i] + 1
			match = D[j-1][i-1]
			
			if A[i - 1] == B[j - 1]:
				D[j][i] = match
			else:
				D[j][i] = min(insertion, deletion)

	# new_A = []
	# new_B = []
	# i, j  = n, m
	# while i or j:
	# 	if i > 0 and D[j][i] == D[j][i - 1] + 1:
	# 		print('i')
	# 		new_A = [A[i - 1]] + new_A
	# 		new_B = ['-'] + new_B
	# 		i -= 1
	# 	elif j > 0 and D[j][i] == D[j - 1][i] + 1:
	# 		print('j')
	# 		new_A = ['-'] + new_A
	# 		new_B = [B[j - 1]] + new_B
	# 		j -= 1
	# 	else:
	# 		print('both')
	# 		new_A = [A[i - 1]] + new_A
	# 		new_B = [B[j - 1]] + new_B
	# 		i -= 1
	# 		j -= 1

	# count = 0
	# for i in range(len(new_A)):
	# 	if new_A[i] == new_B[i]:
	# 		count += 1
	
	# print(new_A)
	# print(new_B)
	# print(D)
	# return new_A, new_B, count
	
	count = 0
	while n > 0 or m > 0:
		if n > 0 and D[m][n] == D[m][n - 1] + 1:
			n -= 1
		elif m > 0 and D[m][n] == D[m - 1][n] + 1:
			m -= 1
		else:
			n -= 1
			m -= 1
			if A[n] == B[m]:
				count += 1
	return count



if __name__ == '__main__':
	n = input()
	A = input().split()
	
	m = input()
	B = input().split()

	# A = 'e d i t i n g'.split()
	# B = 'd i s t a n c e'.split()


	# A = '2 7 8 3'.split()
	# B = '5 2 8 7'.split()
	print(common_seq(A, B))
	# new_A, new_B, count = common_seq(A, B)
	# print(new_A)
	# print(new_B)
	# print(count)

