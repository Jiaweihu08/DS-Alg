def money_change(m):
	coins_used = 0
	while m != 0:
		if m >= 10:
			coins_used += m // 10
			m = m % 10
		elif m >= 5:
			coins_used += m // 5
			m = m % 5
		else:
			return coins_used + m
	return coins_used 


if __name__ == '__main__':
	m = int(input())
	print(money_change(m))