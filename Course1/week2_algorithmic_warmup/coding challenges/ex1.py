def table_fib(n):
	fib = [0] * (n+2)
	fib[1] = 1
	for i in range(2, n+1):
		fib[i] = fib[i - 1] + fib[i - 2]
	return fib[n]

if __name__ == '__main__':
	n = int(input())
	print(table_fib(n))