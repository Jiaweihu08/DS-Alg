#python3

def BWT(text):
	n = len(text)
	matrix = []
	for i in reversed(range(n)):
		matrix.append(text[i:n])
	for sub in sorted(matrix):
		print(n-len(sub), end=' ')






if __name__ == '__main__':
	# text = input().strip()
	text = 'AACGATAGCGGTAGA$'
	BWT(text)