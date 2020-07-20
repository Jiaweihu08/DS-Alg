import itertools

def partitioning_3(A):
	total = sum(A)
	if total % 3 != 0:
		return 0
	
	n = len(A)
	target = total // 3
	S = [[0] * (target + 1) for _ in range(n + 1)]

	for s in S:
		s[0] = True
	for i in range(1, target + 1):
		S[0][i] = False

	for i in range(1, n + 1):
		for j in range(1, target + 1):
			if j - A[i - 1] >= 0:
				S[i][j] = S[i - 1][j] or S[i - 1][j - A[i - 1]]
			else:
				S[i][j] = S[i - 1][j]

	return int(S[-1][-1])

if __name__ == '__main__':
	n = int(input())
	A = list(map(int, input().split()))
	# A = list(map(int, '3 3 3 3'.split()))
	print(partitioning_3(A))