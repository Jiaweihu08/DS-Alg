def max_gold(W, weights):
	n = len(weights)
	values = [[0] * (W + 1) for _ in range(n + 1)]

	for i in range(1, n + 1):
		for w in range(1, W + 1):
			values[i][w] = values[i - 1][w]
			if weights[i - 1] <= w:
				val = values[i - 1][w - weights[i - 1]] + weights[i - 1]
				if val > values[i][w]:
					values[i][w] = val
	return values[-1][-1]

if __name__ == '__main__':
	W, n = map(int, input().split())
	weights = list(map(int, input().split()))
	print(max_gold(W, weights))