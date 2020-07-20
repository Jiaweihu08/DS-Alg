# def majority_element(A):
# 	# scan it once using a dicctionary
#	# running time O(n)
# 	n = len(A)
# 	d = dict()
# 	for i in range(len(A)):
# 		num = A[i]
# 		if num in d:
# 			d[num] += 1
# 			if d[num] > int(n / 2):
# 				return 1
# 		else:
# 			d[num] = 1
# 	return 0

def is_candidate(A, l, r, candidate):
	count = 0
	for num in A[l:r]:
		if num == candidate:
			count += 1
	if count > int(len(A[l:r]) / 2):
		return candidate
	return -1

def majority_element(A, l, r):
	if len(A[l:r]) in (1, 2):
		return is_candidate(A, l, r, A[l])

	m = int(l + (r - l + 1) / 2)
	left_cand = majority_element(A, l, m)
	right_cand = majority_element(A, m, r)

	cands = [cand for cand in (left_cand, right_cand) if cand != -1]
	for cand in cands:
		candidate = is_candidate(A, l, r, cand)
		if candidate != -1:
			return candidate
	return -1


if __name__ == '__main__':
	a = int(input())
	A = list(map(int, input().split()))
	if majority_element(A, 0, len(A)) != -1:
		print(1)
	else:
		print(0)
