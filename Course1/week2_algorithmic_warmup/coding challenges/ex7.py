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

	boundaries = sum(p_period[remainder_m:]) + sum(p_period[:remainder_n])
	center = sum(p_period) * (num_periods_n - max(1, num_periods_m))
	out = boundaries % 10 + center % 10
	return out % 10

if __name__ == '__main__':
	m, n = map(int, input().split())
	print(last_digit_partial_sum_fib(m, n))