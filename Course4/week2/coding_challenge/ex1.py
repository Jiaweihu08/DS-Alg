#python3

def bwt(text):
	n = len(text)
	matrix = []
	for i in reversed(range(n)):
		matrix.append(text[i:n] + text[:i])
	matrix.sort()
	for rotation in matrix:
		print(rotation[-1], end='')

if __name__ == '__main__':
	text = input()
	# text = 'ACA$'
	bwt(text)