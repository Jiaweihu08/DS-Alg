def binary_search(A, l, h, num):
	while l < h:
		m = int(l + (h - l) / 2)
		if A[m] == num:
			return m
		elif A[m] > num:
			h = m
		else:
			l = m + 1
	return -1

def ex1(a, A, b, B):
	return [binary_search(A, 0, a, j) for j in B]


if __name__ == '__main__':
	a, *A = map(int, input().split())
	b, *B = map(int, input().split())
	print(*ex1(a, A, b, B))
