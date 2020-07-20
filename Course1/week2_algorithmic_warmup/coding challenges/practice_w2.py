def naive_fib(n):
	if n <= 1:
		return n
	return naive_fib(n - 1) + naive_fib(n - 2)

def table_fib(n):
	fib = [0] * (n+2)
	fib[1] = 1
	for i in range(2, n+1):
		fib[i] = fib[i - 1] + fib[i - 2]
	return fib[n]

def fib_last_digit(n):
	fib = [0] * (n+1)
	fib[1] = 1
	for i in range(2, n+1):
		fib_i = fib[i - 1] + fib[i - 2]
		fib[i] = fib_i % 10
	return fib[-1]

def euclidian_gcd(a, b):
	if b == 0:
		return a
	return euclidian_gcd(b, a % b)

def lcm(a, b):
	return int(a*b/euclidian_gcd(a,b))

def fib_num_mod(n, m):
	p_period = [0, 1]
	p_len = 0
	while True:
		p_period.append((p_period[-1] + p_period[-2]) % m)
		if p_period[-2:] == [0, 1]:
			p_len = len(p_period) - 2
			break
	return table_fib(n % p_len) % m

def last_digit_sum_fib(n):
	p_period = [0, 1]
	p_len = 0
	while True:
		p_period.append((p_period[-1] + p_period[-2]) %10)
		if p_period[-2:] == [0, 1]:
			p_period = p_period[:-2]
			p_len = len(p_period)
			break
	remainder = n % p_len + 1
	num_periods = n // p_len
	out = sum(p_period) * num_periods + sum(p_period[:remainder])
	return out % 10


def last_digit_partial_sum_fib(m, n):
	p_period = [0, 1]
	p_len = 0
	while True:
		p_period.append((p_period[-1] + p_period[-2]) %10)
		if p_period[-2:] == [0, 1]:
			p_period = p_period[:-2]
			p_len = len(p_period)
			break
	remainder_n = n % p_len + 1
	remainder_m = m % p_len
	num_periods_n = n // p_len - 1
	num_periods_m = m // p_len

	boundaries = sum(period[remainder_m:]) + sum(period[:remainder_n])
	center = sum(period) * (num_periods_n - max(1, num_periods_m))
	out = boundaries % 10 + center % 10
	return out % 10

def last_digit_sum_square_fib(n):
	p_period = [0, 1]
	p_len = 0
	while True:
		p_period.append((p_period[-1] + p_period[-2]) %10)
		if p_period[-2:] == [0, 1]:
			p_period = [i**2 for i in p_period[:-2]]
			p_len = len(p_period)
			break
	remainder = n % p_len + 1
	num_periods = n // p_len
	out = sum(p_period) * num_periods + sum(p_period[:remainder])
	return out % 10


if __name__ == '__main__':
	n = int(input())
	# print(naive_fib(n))
	print(table_fib(n))

	n = int(input())
	print(fib_last_digit(n))
	
	a, b = map(int, input().split())
	print(euclidian_gcd(a, b))

	a, b = map(int, input().split())
	print(lcm(a, b))

	n, m = map(int, input().split())
	print(fib_num_mod(n, m))

	n = int(input())
	print(last_digit_sum_fib(n))

	m, n = map(int, input().split())
	print(last_digit_partial_sum_fib(m, n))

	n = int(input())
	print(last_digit_sum_square_fib(n))


