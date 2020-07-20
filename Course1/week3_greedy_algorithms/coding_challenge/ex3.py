def car_fueling(d, m, n, stops):
	stops = [0] + stops + [d]
	num_refills, current_refill = 0, 0
	while current_refill <= n:
		last_refill = current_refill
		while (current_refill <= n and
			stops[current_refill + 1] - stops[last_refill] <= m):
			current_refill += 1
		if current_refill == last_refill:
			return -1
		if current_refill <= n:
			num_refills += 1
	return num_refills


if __name__ == '__main__':
	d = int(input())
	m = int(input())
	n = int(input())
	stops = list(map(int, input().split()))
	print(car_fueling(d, m, n, stops))
