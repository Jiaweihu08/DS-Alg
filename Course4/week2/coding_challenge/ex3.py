#python3


def preprocess_bwt(bwt):
	n = len(bwt)
	sorted_text = sorted(bwt)
	starts = {'$':0, 'A':1, 'C':None, 'G':None, 'T':None}
	occ_count_before = {'$': [0] * (n + 1),
						'A': [0] * (n + 1),
						'C': [0] * (n + 1),
						'G': [0] * (n + 1),
						'T': [0] * (n + 1)}
	for i in range(n):
		if starts[sorted_text[i]] == None:
			starts[sorted_text[i]] = i
		for key in occ_count_before.keys():
			if key == bwt[i]:
				occ_count_before[key][i + 1] = occ_count_before[key][i] + 1
			else:
				occ_count_before[key][i + 1] = occ_count_before[key][i]

	return starts, occ_count_before

def count_occurrences(pattern, bwt, starts, occ_count_before):
	top = 0
	bottom = len(bwt) - 1
	pointer = len(pattern) - 1
	while top <= bottom:
		if pointer >= 0:
			symbol = pattern[pointer]
			pointer -= 1
			if occ_count_before[symbol][top] != occ_count_before[symbol][bottom + 1]:
				top = starts[symbol] + occ_count_before[symbol][top]
				bottom = starts[symbol] + occ_count_before[symbol][bottom + 1] - 1
			else:
				return 0
		else:
			return bottom - top + 1



if __name__ == '__main__':
	bwt = input().strip()
	n = int(input())
	patterns = input().strip().split()

# 	lines = '''TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC
# 5
# CCT CACA GAG CAG ATC'''.split('\n')

# 	lines = '''AT$TCTATG
# 2
# ATC TATG'''.split('\n')
	# bwt = lines[0]
	# n = int(lines[1])
	# patterns = lines[2].split()

	# print('\nbwt:', bwt, '\n')
	# original = inverting_bwt(bwt)
	# print('original text:', original, '\n')
	# # print('patterns:', patterns, '\n')
	# print('sorted text:', ''.join(sorted(bwt)), '\n')
	

	starts, occ_count_before = preprocess_bwt(bwt)
	# print('starts:\n', starts, '\n')
	# print('occ_counts:')
	# for pair in occ_count_before.items():
	# 	print(pair)

	occurrences_counts = [count_occurrences(pattern, bwt, starts, occ_count_before)
							for pattern in patterns]
	print(' '.join(map(str, occurrences_counts)))




