def table_fib(n):
	fib = [0] * (n+2)
	fib[1] = 1
	for i in range(2, n+1):
		fib[i] = fib[i - 1] + fib[i - 2]
	return fib[n]

def fib_num_mod(n, m):
	p_period = [0, 1]
	p_len = 0
	while True:
		p_period.append((p_period[-1] + p_period[-2]) % m)
		if p_period[-2:] == [0, 1]:
			p_len = len(p_period) - 2
			break
	return table_fib(n % p_len) % m


if __name__ == '__main__':
	n, m = map(int, input().split())
	print(fib_num_mod(n, m))