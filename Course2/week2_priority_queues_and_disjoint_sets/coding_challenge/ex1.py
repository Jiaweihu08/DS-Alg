def build_heap(a):
	n = len(a)
	swaps = []
	for i in reversed(range(n // 2)):
		while i < n:
			indice = i
			l = 2 * i + 1
			if l < n and a[l] < a[indice]:
				indice = l

			r = 2 * i + 2
			if r < n and a[r] < a[indice]:
				indice = r
			if indice != i:
				a[indice], a[i] = a[i], a[indice]
				swaps.append((i, indice))
				i = indice
			else:
				break
	return swaps


if __name__ == '__main__':
	n = int(input())
	a = list(map(int, input().split()))
	# a = [5,4,3,2,1,0]
	swaps = build_heap(a)
	print(len(swaps))
	for swap in swaps:
		print(*swap)
