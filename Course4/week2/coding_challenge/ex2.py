#python3

# def inverting_bwt_naive(bwt):
# 	n = len(bwt)
# 	col = sorted(bwt)
# 	bwt = list(bwt)
# 	for _ in range(n - 1):
# 		col = map(''.join, sorted(zip(bwt, col)))
# 	return list(col)[0][1:] + '$'

def inverting_bwt(bwt):
	n = len(bwt)
	first_col = sorted(bwt)
	last_col = list(bwt)

	pos_1, pos_n = {}, {}
	ocurr_1, ocurr_n = {}, {}
	
	for letter in set(last_col):
		ocurr_1[letter], ocurr_n[letter] = 1, 1
	
	for i in range(n):
		symbol_1, symbol_n = first_col[i], last_col[i]
		c1, cn = ocurr_1[symbol_1], ocurr_n[symbol_n]
		ocurr_1[symbol_1] += 1
		ocurr_n[symbol_n] += 1
		k1, kn = '{}_{}'.format(symbol_1, c1), '{}_{}'.format(symbol_n, cn)
		pos_1[k1], pos_n[kn] = i, i
		first_col[i], last_col[i] = k1, kn
	
	symbol = first_col[0]
	text = ''
	for _ in range(n):
		symbol = first_col[pos_n[symbol]]
		text += symbol[0]
	return text



if __name__ == '__main__':
	bwt = input()
	# bwt = 'SMNPBNNAAAAA$A'
	# naive_output = inverting_bwt_naive(bwt)
	# print(naive_output)
	print(inverting_bwt(bwt))

	