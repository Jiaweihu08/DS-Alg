def merge_and_count(B, C):
	D = list()
	count = 0
	while B and C:
		if B[0] > C[0]:
			count += len(B)
			D.append(C.pop(0))
		else:
			D.append(B.pop(0))
	if B:
		D.extend(B)
	else:
		D.extend(C)
	return D, count

def merge_sort_and_count_inv(A):
	n = len(A)
	if n == 1:
		return A, 0
	m = (n + 1) // 2
	B, num_pairs_b = merge_sort_and_count_inv(A[:m])
	C, num_pairs_c = merge_sort_and_count_inv(A[m:])
	D, count = merge_and_count(B, C)

	num_inv = count + num_pairs_b + num_pairs_c
	# print(num_inv)
	return D, num_inv



if __name__ == '__main__':
	n = input()
	A = list(map(int, input().split()))
	sorted_arr, inv_counts = merge_sort_and_count_inv(A)
	print(inv_counts)
