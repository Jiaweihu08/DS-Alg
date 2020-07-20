def edit_dist(A, B):
	n = len(A)
	m = len(B)
	D = [[m] + [i for i in range(1, n + 1)] for m in range(m + 1)]

	for j in range(1, m + 1):
		for i in range(1, n + 1):
			insertion = D[j][i-1] + 1
			deletion = D[j-1][i] + 1
			match = D[j-1][i-1]
			mismatch = D[j-1][i-1] + 1
			
			if A[i - 1] == B[j - 1]:
				D[j][i] = min(insertion, deletion, match)
			else:
				D[j][i] = min(insertion, deletion, mismatch)
	return D[m][n]

if __name__ == '__main__':
	A = input().strip()
	B = input().strip()

	# A = 'editing'
	# B = 'distance'
	
	edit_dist = edit_dist(A, B)
	print(edit_dist)