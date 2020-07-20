def dp_knapsack_no_rep(W, weights, values):
	n = len(values)
	value = [[0] * (W + 1) for _ in range(n + 1)]

	for i in range(1, n + 1):
		for w in range(1, W + 1):
			value[i][w] = value[i - 1][w]
			if weights[i - 1] <= w:
				val = value[i - 1][w - weights[i - 1]] + values[i - 1]
				if val > value[i][w]:
					value[i][w] = val
					
	return value[-1][-1]


if __name__ == '__main__':
	W = 10
	weights = [6, 3, 4, 2]
	values = [30, 14, 16, 9]
	print(dp_knapsack_no_rep(W, weights, values))