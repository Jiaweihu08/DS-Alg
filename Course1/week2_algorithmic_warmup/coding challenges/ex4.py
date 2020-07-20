def euclidian_gcd(a, b):
	if b == 0:
		return a
	return euclidian_gcd(b, a % b)

def lcm(a, b):
	return int(a*b/euclidian_gcd(a,b))


if __name__ == '__main__':
	a, b = map(int, input().split())
	print(lcm(a, b))