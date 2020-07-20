from random import randint


def poly_hash(P, p, x):
	h = 0
	for i in reversed(range(len(P))):
		h = (h * x + ord(P[i])) % p
	return h

def precompute_hashes(T, len_p, p, x):
	len_t = len(T)
	n = len_t - len_p + 1

	hashes = [None] * n
	s = T[len(T) - len_p:]
	hashes[-1] = poly_hash(s, p, x)
	y = 1
	for i in range(len_p):
		y = (y * x) % p

	for i in reversed(range(n - 1)):
		hashes[i] = (x * hashes[i + 1] + ord(T[i]) - y * ord(T[i + len_p])) % p
	return hashes

def rabin_karp(T, P):
	p = 7 + 10**12
	x = randint(1, p - 1)
	result = []
	p_hash = poly_hash(P, p, x)
	hashes = precompute_hashes(T, len(P), p, x)
	for i in range(len(T) - len(P) + 1):
		h = hashes[i]
		if p_hash != h:
			continue
		if T[i:i + len(P)] == P:
			result.append(i)
	return result

def main():
	P = input()
	T = input()
	# T = 'testTesttesT'
	# P = 'Test'
	print(*rabin_karp(T, P))



if __name__ == '__main__':
	main()