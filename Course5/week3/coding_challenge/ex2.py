#python3
from itertools import product, combinations
import sys


def varnum(i, j):
	return str(i) + '-' + str(j)


def get_var_num_dict(n):
	count = 1
	num_to_var = {}
	r = range(1, n + 1)
	for pair in product(r, r):
		num_to_var[varnum(*pair)] = count
		count += 1
	return num_to_var


def exactly_one_of(literals, num_to_var, clauses, only_neg=False):
	clause_to_add = [num_to_var[l] for l in literals]
	if not only_neg:
		clauses.append(clause_to_add)
	for pair in combinations(clause_to_add, 2):
		clauses.append([-l for l in pair])


def main(lines):
	n, m = map(int, lines[0].split())
	r = range(1, n + 1)
	# edges = [list(map(int, line.split())) for line in lines[1:]]
	graph = [[i] for i in r]
	for line in lines[1:]:
		u, v = map(int, line.split())
		graph[u - 1].append(v)
		graph[v - 1].append(u)

	num_to_var = get_var_num_dict(n)
	clauses = []
	for i in r:
		exactly_one_of([varnum(*pair) for pair in zip([i] * n, r)],
						num_to_var,
						clauses)
	for i in r:
		exactly_one_of([varnum(*pair) for pair in zip(r, [i] * n)],
						num_to_var,
						clauses)

	# for e in edges:
	# 	for k in range(1, n):
	# 		literals = [varnum(*pair) for pair in zip(e, [k, k + 1])]
	# 		clauses.append([num_to_var[l] for l in literals])

	# 		literals = [varnum(*pair) for pair in zip(e, [k + 1, k])]
	# 		clauses.append([num_to_var[l] for l in literals])

	for i, j in combinations(r, 2):
		if j in graph[i - 1]:
			continue
		for k in range(1, n):
			exactly_one_of([varnum(*pair) for pair in zip((i, j), [k, k + 1])],
							num_to_var,
							clauses,
							True)
			exactly_one_of([varnum(*pair) for pair in zip((i, j), [k + 1, k])],
							num_to_var,
							clauses,
							True)

	print(len(clauses), len(num_to_var))
	for clause in clauses:
		clause += [0]
		print(*clause)

	# var_to_num = {var:num for num, var in num_to_var.items()}
	# for clause in clauses:
	# 	sign = 1 if clause[0] > 0 else -1
	# 	to_print = [var_to_num[abs(c)] * sign for c in clause]# + [0]
	# 	print(*to_print)

	# print(num_to_var)
	# print(graph)

if __name__ == '__main__':
	lines = sys.stdin.read().strip().split('\n')
# 	lines = '''5 4
# 1 2
# 2 3
# 3 5
# 4 5'''.split('\n')
	main(lines)
