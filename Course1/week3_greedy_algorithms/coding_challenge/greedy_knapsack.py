def greedy_knapsack(W, weights, values):
	# assuming values[i]/weights[i] > values[i+1]/weigths[i+1]
	n = len(weights)
	V = 0
	A = [0]	* n
	
	for i in range(n):
		if W == 0:
			return V, A
		a = min(weights[i], W)
		V += a * values[i] / weights[i]
		weights[i] -= a
		A[i] += a
		W -= a
	return V, A

