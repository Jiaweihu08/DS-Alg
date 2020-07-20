#python3

def compute_prefix(p):
	s = [0]
	border = 0
	for i in range(1, len(p)):
		while border > 0 and p[i] != p[border]:
			border = s[border - 1]
		if p[i] == p[border]:
			border += 1
		else:
			border = 0
		s.append(border)
	return s

def find_all_occ(p, T):
	n = len(p)
	S = p + '$' + T
	s = compute_prefix(S)
	result = [i - 2 * n for i in range(n + 1, len(S)) if s[i] == n]
	return result


if __name__ == '__main__':
	p = input().strip()
	T = input().strip()
	result = find_all_occ(p, T)
	print(*result)
