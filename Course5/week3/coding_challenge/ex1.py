#python3
from itertools import combinations, product
import sys


def varnum(i, j):
	return 10 * i + j

def get_vars(n):
	var_dict = {}
	count = 1

	for pair in product(range(1, n + 1), range(1, 4)):
		var_dict[varnum(*pair)] = count
		count +=1
	return var_dict

def exactly_one_of(literals, var_dict, clauses, is_edge=False):
	clause_to_add = [var_dict[l] for l in literals]
	if not is_edge:
		clauses.append(clause_to_add)
	
	for pair in combinations(clause_to_add, 2):
		clauses.append([-l for l in pair])

def main(lines):
	n, m = map(int, lines[0].split())
	edges = [list(map(int, line.split())) for line in lines[1:]]
	color_digits = range(1,4)
	clauses = []
	var_dict = get_vars(n)

	for i in range(1, n + 1):
		exactly_one_of([varnum(i, j) for j in color_digits],
						var_dict,
						clauses)

	for e in edges:
		for i in color_digits:
			exactly_one_of([varnum(*pair) for pair in zip(e, [i]*2)],
							var_dict,
							clauses, True)

	# var_to_index = {v:k for k, v in var_dict.items()}
	print(len(clauses), len(var_dict))
	for clause in clauses:
		clause += [0]
		print(*clause)

		# sign = 1 if clause[0] > 0 else -1
		# to_print = [var_to_index[abs(c)]*sign for c in clause] + [0]
		# print(*to_print)


if __name__ == '__main__':
	lines = sys.stdin.read().strip().split('\n')
# 	lines = '''3 3
# 1 2
# 2 3
# 1 3'''.split('\n')
	main(lines)

