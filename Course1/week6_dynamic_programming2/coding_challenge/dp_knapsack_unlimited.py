def dp_knapsack_unlimited(W, values, weights):
	n = len(weights)
	V = [0] * (W + 1)
	for w in range(1, W + 1):
		for i in range(n):
			if weights[i] <= w:
				val = V[w - weights[i]] + values[i]
				if val > V[w]:
					V[w] = val
	return V[-1]

if __name__ == '__main__':
	W = 10
	values = [30, 14, 16, 9]
	weights = [6, 3, 4, 2]
	print(dp_knapsack_unlimited(W, values, weights))
