def fib_last_digit(n):
	fib = [0] * (n+1)
	fib[1] = 1
	for i in range(2, n+1):
		fib_i = fib[i - 1] + fib[i - 2]
		fib[i] = fib_i % 10
	return fib[-1]

if __name__ == '__main__':
	n = int(input())
	print(fib_last_digit(n))
