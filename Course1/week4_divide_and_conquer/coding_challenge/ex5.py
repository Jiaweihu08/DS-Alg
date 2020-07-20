# import random
import sys


# def naive_count_segments(segments, points):
# 	s, p = len(segments), len(points)
# 	counts = [0] * p
# 	for i in range(p):
# 		for segment in segments:
# 			if segment[0] <= points[i] <= segment[1]:
# 				counts[i] += 1
# 	return counts

# def false_fast_count_segments(segments, points):
# 	s = len(segments)
# 	p = len(points)
# 	segments = sorted(segments, key=lambda x: x[1])
# 	points = sorted(list(enumerate(points)), key=lambda x: x[1])
# 	counts = [0] * p
# 	e = 0
# 	for i in range(p):
# 		for j in range(e, s):
# 			if points[i][1] > segments[j][1]:
# 				e += 1
# 				continue
# 			elif segments[j][0] <= points[i][1] <= segments[j][1]:
# 				counts[points[i][0]] += 1
# 	return counts

def merge(B, C):
	merge = list()
	while B and C:
		b = B[0]
		c = C[0]
		if b[0] > c[0]:
			merge.append(C.pop(0))
		elif b[0] == c[0]:
			if b[1] < c[1]:
				merge.append(B.pop(0))
			else:
				merge.append(C.pop(0))
		else:
			merge.append(B.pop(0))
	if B:
		merge.extend(B)
	else:
		merge.extend(C)
	return merge

def merge_sort(A):
	n = len(A)
	if n == 1:
		return A
	m = (n + 1) // 2
	B = merge_sort(A[:m])
	C = merge_sort(A[m:])
	D = merge(B, C)
	return D

def fast_count_segments(stars, ends, points):
	counts = [0] * len(points)
	all_pairs = []
	for i in range(len(stars)):
		all_pairs.append((stars[i], 'l'))
		all_pairs.append((ends[i], 'r'))
	for j in range(len(points)):
		all_pairs.append((points[j], 'p', j))

	sorted_pairs = merge_sort(all_pairs)
	count = 0
	for pair in sorted_pairs:
		if pair[1] == 'l':
			count += 1
		elif pair[1] == 'p':
			counts[pair[2]] = count
		else:
			count -= 1
	return counts



# def get_data(s, p):
# 	segments = []
# 	data = []
# 	for _ in range(s):
# 		a, b = random.randint(0, 20), random.randint(0, 9)
# 		data.extend([a, a + b])
# 		segments.append((a, a + b))

# 	starts = data[0:2 * s + 2:2]
# 	ends = data[1:2 * s + 2:2]
# 	points = [random.randint(0, 20) + 3 for _ in range(p)]
# 	return segments, starts, ends, points

# def stress_test(num_tests, s, p):
# 	counts = 0
# 	print('\n', '-' * 5, 'Test cases', '-' * 5)
# 	for i in range(num_tests):
# 		segments, starts, ends, points = get_data(s, p)
# 		naive_counts = naive_count_segments(segments, points)
# 		fast_counts = fast_count_segments(starts, ends, points)

# 		if naive_counts != fast_counts:
# 			print("\n---> Wrong answer!")
# 			print("Segments: {}\nPoints: {}\n-".format(segments, points))
# 			print("Expected output: {}".format(naive_counts))
# 			print("Your output: {}\n--------".format(fast_counts))
# 		else:
# 			counts += 1
# 	print("\nTotal number of correct predictions: {}/{}".\
# 			format(counts, num_tests))



if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n = data[0]
	m = data[1]
	starts = data[2:2 * n + 2:2]
	ends = data[3:2 * n + 2:2]
	points = data[2 * n + 2:]

	# starts = [0,-3,7]
	# ends = [5,2,10]
	# points = [1,6]

	# starts = [4,2]
	# ends = [10,6]
	# points = [5,8,3]

	counts = fast_count_segments(starts, ends, points)
	print(*counts)

	# stress_test(20, 20, 10)




