def helping_thief(n, W, l):
	ratio = [p[0]/p[1] for p in l]
	sorted_ratio = sorted(enumerate(ratio), key=lambda x: x[1], reverse=True)
	sorted_index = [p[0] for p in sorted_ratio]
	
	value = 0
	for i in sorted_index:
		if W == 0:
			return value
		fraction = min(l[i][1], W)
		value += fraction * ratio[i]
		W -= fraction
	return value

def get_vms():
	v, w = map(int, input().split())
	return v, w


if __name__ == '__main__':
	n, W = map(int, input().split())
	l = [get_vms() for _ in range(n)]
	print('{:.4f}'.format(helping_thief(n, W, l)))