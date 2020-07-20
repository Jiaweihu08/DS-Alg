# def collect_signatures(segs):
# 	segs = sorted(segs, key=lambda x: (x[0], x[1]))
# 	points = []
# 	while segs:
# 		current_a = segs[0][0]
# 		current_b = p = segs[0][1]
# 		for seg in segs[1:]:
# 			if seg[1] < p:
# 				current_b = min(seg[1], current_b)
# 			elif seg[0] == current_a:
# 				continue
# 			else:
# 				break
# 		for seg in segs.copy():
# 			if seg[0] <= current_b and seg[1] >= current_b:
# 				segs.remove(seg)
# 			else:
# 				break
# 		points.append(current_b)
# 	return len(points), points


def collect_signatures(segs):
	segs = sorted(segs, key=lambda x: x[1])
	# print(segs)
	points = []
	n = len(segs) - 1
	i = 0
	while i <= n:
		b = segs[i][1]
		points.append(b)
		i += 1
		while i <= n and segs[i][0] <= b <= segs[i][1]:
			i += 1
	return len(points), points

def get_abs():
	a, b = map(int, input().split())
	return a, b

	
if __name__ == '__main__':
	n = int(input())
	segs = [get_abs() for _ in range(n)]
	# segs = [(2,3),(4,5),(1,7),(1,6)]
	# segs = [(1,5),(1,6),(2,3),(3,4),(5,7),(6,7)]
	# segs = [(1,2),(3,6),(3,7),(4,6),(4,5),(6,10),(7,8),(7,9)]
	# segs = [(4,7),(1,3),(2,5),(5,6)]
	num_points, points = collect_signatures(segs)
	print(num_points)
	print(*points)