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

if __name__ == '__main__':
	n = int(input())
	print(last_digit_sum_fib(n))