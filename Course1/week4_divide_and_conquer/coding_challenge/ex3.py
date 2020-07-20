import random


def partition3(A, l, r):
	x = A[l]
	m2 = l
	m1 = list()
	for i in range(l + 1, r):
		if A[i] <= x:
			m2 += 1
			A[i], A[m2] = A[m2], A[i]

			if A[m2] == x:
				m1.append(m2)

	A[l], A[m2] = A[m2], A[l]

	not_x = [num for num in A[m2-len(m1):m2] if num != x]
	if not_x:
		e = 0
		for i in range(l, m2-len(m1)):
			if A[i] == x:
				A[i] = not_x[e]
				e += 1
		A[m2-len(m1):m2] = [x] * len(m1)

	return m2 - len(m1), m2

def randomized_quick_sort(A, l, r):
	if l >= r:
		return
	k = random.randint(l, r - 1)
	A[l], A[k] = A[k], A[l]
	m1, m2 = partition3(A, l, r)
	randomized_quick_sort(A, l, m1)
	randomized_quick_sort(A, m2 + 1, r)



if __name__ == '__main__':
	n = int(input())
	A = list(map(int, input().split()))
	randomized_quick_sort(A, 0, len(A))
	print(*A)



	# num_cases = 10
	# case_len = 1000
	# A =[[random.randint(100000000,100000005) for _ in range(case_len)] \
	# 		for _ in range(num_cases)]

	# count = 0
	# for a in A:
	# 	# print(a)
	# 	sorted_a = sorted(a)
	# 	randomized_quick_sort(a, 0, len(a))
	# 	if sorted_a != a:
	# 		print('Wrong Answer!')
	# 		print(*a)
	# 	else:
	# 		count += 1
	# print("Correct cases: {}/{}".format(count, num_cases))





