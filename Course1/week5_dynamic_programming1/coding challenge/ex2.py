def primitive_calculator(n):
	moves = [[]]
	
	for j in range(1, n + 1):
		last_pos = j - 1
		min_num_ops = len(moves[last_pos])
		
		if j % 2 == 0 and len(moves[j // 2]) < min_num_ops:
			last_pos = j // 2
			min_num_ops = len(moves[last_pos])
		
		if j % 3 == 0 and len(moves[j // 3]) < min_num_ops:
			last_pos = j // 3
			min_num_ops = len(moves[last_pos])
		
		moves.append(moves[last_pos] + [j])
	
	return moves[-1]


if __name__ == '__main__':
	n = int(input())
	# n = 96234
	moves = primitive_calculator(n)
	# print(n)
	print(len(moves)-1)
	print(*moves)