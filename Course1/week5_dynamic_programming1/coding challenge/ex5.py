def common_seq(A, B, C):
	n = len(A)
	m = len(B)
	l = len(C)
	D = [[[j] + [j + k for k in range(1, l + 1)]] + \
			[[i + j] + [0 for _ in range(1, l + 1)] for i in range(1, n + 1)]
				for j in range(m + 1)]

	for i in range(1, n + 1):
	    for k in range(1, l + 1):
	        D[0][i][k] = i + k

	for j in range(1, m + 1):
		for i in range(1, n + 1):
			for k in range(1, l + 1):
				del_l = D[j][i][k - 1] + 1
				del_n = D[j][i - 1][k] + 1
				del_m = D[j - 1][i][k] + 1

				if A[i - 1] == B[j - 1] == C[k- 1]:
					D[j][i][k] = D[j - 1][i - 1][k - 1]
				else:
					D[j][i][k] = min(del_l, del_n, del_m)

	# new_A = []
	# new_B = []
	# new_C = []
	# while m > 0 or n > 0 or l > 0:
	# 	if l > 0 and D[m][n][l] == D[m][n][l - 1] + 1:
	# 		l -= 1
	# 		new_C = [C[l]] + new_C
	# 		new_A = ['-'] + new_A
	# 		new_B = ['-'] + new_B

	# 	elif n > 0 and D[m][n][l] == D[m][n - 1][l] + 1:
	# 		n -= 1
	# 		new_A = [A[n]] + new_A
	# 		new_B = ['-'] + new_B
	# 		new_C = ['-'] + new_C

	# 	elif m > 0 and D[m][n][l] == D[m - 1][n][l] + 1:
	# 		m -= 1
	# 		new_B = [B[m]] + new_B
	# 		new_A = ['-'] + new_A
	# 		new_C = ['-'] + new_C
		
	# 	else:
	# 		m -=1
	# 		n -=1
	# 		l -=1
	# 		new_A = [A[n]] + new_A
	# 		new_B = [B[m]] + new_B
	# 		new_C = [C[l]] + new_C 
	# # print(new_A)
	# # print(new_B)
	# # print(new_C)
	# count = 0
	# for i in range(len(new_A)):
	# 	if new_A[i] == new_B[i] == new_C[i]:
	# 		count += 1
	# return new_A, new_B, count
	
	count = 0
	while n > 0 or m > 0 or l > 0:
		if l > 0 and D[m][n][l] == D[m][n][l - 1] + 1:
			l -= 1
		elif n > 0 and D[m][n][l] == D[m][n - 1][l] + 1:
			n -= 1
		elif m > 0 and D[m][n][l] == D[m - 1][n][l] + 1:
			m -= 1
		else:
			l -= 1
			n -= 1
			m -= 1
			if A[n] == B[m] == C[l]:
				count += 1
	return count



if __name__ == '__main__':
	n = input()
	A = input().split()
	
	m = input()
	B = input().split()

	l = input()
	C = input().split()

	# A = '1 2 3'.split()
	# B = '2 1 3'.split()
	# C = '1 3 5'.split()

	# A = '8 3 2 1 7'.split()
	# B = '8 2 1 3 8 10 7'.split()
	# C = '6 8 3 1 4 7'.split()

	print(common_seq(A, B, C))
	# new_A, new_B, count = common_seq(A, B)
	# print(new_A)
	# print(new_B)
	# print(count)