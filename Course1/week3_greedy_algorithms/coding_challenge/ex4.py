def max_ad_revenue(n, A, B):
	A = sorted(A)
	B = sorted(B)
	return sum([A[i] * B[i] for i in range(n)])


if __name__ == '__main__':
	n = int(input())
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))
	print(max_ad_revenue(n, A, B))