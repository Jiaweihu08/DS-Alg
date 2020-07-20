def max_num_prizes(n):
	k = []
	i = 1
	while n >= 2 * i + 1:
		k.append(i)
		n -= i
		i += 1
	k.append(n)
	return len(k), k


if __name__ == '__main__':
	n = int(input())
	num_prizes, prizes = max_num_prizes(n)
	print(num_prizes)
	print(*prizes)