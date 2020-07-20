import math
# from random import randint

def distance(x, y):
	a = (x[0] - y[0]) ** 2
	b = (x[1] - y[1]) ** 2
	return math.sqrt(a + b)

# def naive_min_distance(points):
# 	n = len(points)
# 	min_dist = float('inf')
# 	for i in range(n):
# 		for j in range(i + 1, n):
# 			d = distance(points[i], points[j])
# 			if d < min_dist:
# 				min_dist = d
# 	return min_dist

def merge(B, C, pos):
	merged = []
	while B and C:
		if B[0][pos] > C[0][pos]:
			merged.append(C.pop(0))
		else:
			merged.append(B.pop(0))
	if B:
		merged.extend(B)
	else:
		merged.extend(C)
	return merged

def merge_sort(A, pos=0):
	n = len(A)
	# print('merge_sort, n:', n)
	# print('merge_sort, pos:', pos)
	if n <= 1:
		return A
	m = (n + 1) // 2
	# print('left merge sort')
	B = merge_sort(A[:m], pos=pos)
	# print('right merge sort')
	C = merge_sort(A[m:], pos=pos)
	D = merge(B, C, pos=pos)
	return D

def get_cands_dist(P):
	n = len(P)

	if n == 2:
		# print('---n:',n)
		return P, distance(P[0], P[1])
	elif n == 3:
		# print('---n:',n)
		d1 = distance(P[0], P[1])
		d2 = distance(P[0], P[2])
		d3 = distance(P[1], P[2])
		return P, min(d1, d2, d3)

	m = (n + 1) // 2
	# print("m:",m)
	# print('left recursion')
	points_l, dist_l = get_cands_dist(P[:m])
	# print('right recursion')
	points_r, dist_r = get_cands_dist(P[m:])
	# all_points = points_l + points_r
	d = min(dist_l, dist_r)
	if d == 0:
			return P, 0

	strip_points = []
	middle = (points_l[-1][0] + points_r[0][0]) / 2
	# print('middle', middle)
	for i in range(n):
		if abs(P[i][0] - middle) <= d:
			strip_points.append(P[i])
	
	strip_len = len(strip_points)
	# print('\nnum strip_points:', strip_len)
	if strip_len >= 2:
		sorted_strip = merge_sort(strip_points, pos=1)
		for i in range(strip_len):
			for j in range(i + 1, min(i + 8, strip_len)):
				d_prime = distance(sorted_strip[i], sorted_strip[j])
				if d_prime < d:
					d = d_prime
				else:
					break

	return P, d

def fast_min_distance(P):
	x_sorted = merge_sort(P)
	# print('\nsorted wrt x: ', x_sorted)

	P, d = get_cands_dist(x_sorted)
	# print(cands, d)
	
	# if d == 0 or len(cands) < 2:
	# 	return d


	# print('\nsorting wrt y...\n')

	# sorted_cands = merge_sort(cands, pos=1)
	# n = len(sorted_cands)

	# for i in range(n):
	# 	for j in range(i + 1, min(i + 8, n)):
	# 		d_prime = distance(sorted_cands[i], sorted_cands[j])
	# 		if d_prime < d:
	# 			d = d_prime

	return d

# def stress_test(num_points, num_cases):
# 	point_sets = [[(randint(-100,100), randint(-100,100)) 
# 				for _ in range(randint(num_points - 1, num_points))]
# 				for _ in range(num_cases)]
# 	counts = 0
# 	for points in point_sets:
# 		# print('\n', points)
# 		expected = naive_min_distance(points)
# 		mine_pred = fast_min_distance(points)
# 		if expected != mine_pred:
# 			print('\n' + '-' * 10 + 'Wrong answer' + '-' * 10)
# 			print('Points: {}'.format(points))
# 			print('Expected: {}'.format(expected))
# 			print('Function output: {}'.format(mine_pred))
# 		else:
# 			counts += 1
# 			print('Number of correct outputs: {}\n'.format(counts))
# 	print("\n----- Test finished, number of correct outputs: {}/{} -----".\
# 		format(counts, num_cases))


if __name__ == '__main__':
	n = int(input())
	points = [tuple(map(int, input().split())) for _ in range(n)]

	# points = [(4, 2), (2, 4), (8, 3), (4, 5), (2, 8)]
	# points = [(0, 3), (2, 8), (2, 4), (5, 3), (6, 2),
	# 			(6, 4), (7, 0), (8, 8), (9, 8), (9, 9)]
	# naive_dist = naive_min_distance(points)
	# print('naive min distance: {:.4f}'.format(naive_dist))
	dist = fast_min_distance(points)
	print('{:.4f}'.format(dist))
	# print('faster min distance:{:.4f}'.format(dist))

	# stress_test(num_points=1000, num_cases=10)






