import random


# def partition(A, l, r):
# 	x = A[l]
# 	j = l
# 	for i in range(l + 1, r):
# 		if A[i] <= x:
# 			j += 1
# 			A[i], A[j] = A[j], A[i]
# 	A[l], A[j] = A[j], A[l]
# 	return j

# def quick_sort(A, l, r, random_pivot=True):
# 	if l >= r:
# 		return
# 	if random_pivot:
# 		k = random.randint(l, r - 1)
# 		A[l], A[k] = A[k], A[l]
# 	m = partition(A, l, r)
# 	quick_sort(A, l, m)
# 	quick_sort(A, m + 1, r)

def partition3(A, l, r):
	x = A[l]
	j = l
	d = 0
	for i in range(l + 1, r):
		print(i)
		if A[i] <= x:
			if A[i] == x:
				d += 1
			j += 1
			A[i], A[j] = A[j], A[i]
	A[l], A[j] = A[j], A[l]
	return j - d, j

def quick_sort_3(A, l, r):
	if l >= r:
		return
	# k = random.randint(l, r - 1)
	# A[l], A[k] = A[k], A[l]
	# print(A)
	m1, m2 = partition3(A, l, r)
	print('m1:{}, m2:{}'.format(m1, m2))
	print(A, 'after partition')
	quick_sort_3(A, l, m1)
	quick_sort_3(A, m2 + 1, r)


def test_case():
	arr = [random.randint(1000, 100000) for _ in range(200)]
	return arr, sorted(arr)

if __name__ == '__main__':
	# for _ in range(3):
	# 	arr, sorted_arr = test_case()
	# 	r = len(arr)
	# 	quick_sort(arr, 0, r)
	# 	solution = arr
	# 	if sorted_arr == solution:
	# 		print("\nSorted successfully!\n", arr, '\n', solution, end='\n')
	# 	else:
	# 		print('\nWrong answer!\nArray: {}\nSolution: {}'.format(arr, sorted_arr))
	# 		print('Your solution: {}'.format(solution))

	A = [2,0,1,3,2,2,2,0]
	print(A, 'initial array')
	quick_sort_3(A, 0, len(A))
	solution = A
	print(solution, 'sorted A?')


