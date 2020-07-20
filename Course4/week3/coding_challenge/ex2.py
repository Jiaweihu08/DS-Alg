#python3

def sort_chars(s):
	n = len(s)
	order = [0] * n
	chars = ('$', 'A', 'C', 'G', 'T')
	count = {}
	for char in chars:
		count[char] = 0
	for i in range(n):
		count[s[i]] += 1
	for j in range(1, len(chars)):
		count[chars[j]] += count[chars[j - 1]]
	for i in reversed(range(n)):
		c = s[i]
		count[c] -= 1
		order[count[c]] = i
	return order

def compute_char_classes(s, order):
	n = len(s)
	class_ = [0] * n
	class_[order[0]] = 0
	for i in range(1, n):
		if s[order[i]] != s[order[i - 1]]:
			class_[order[i]] = class_[order[i - 1]] + 1
		else:
			class_[order[i]] = class_[order[i - 1]]
	return class_

def sort_doubled(s, l, order, class_):
	n = len(s)
	count = [0] * n
	new_order = [0] * n
	for i in range(n):
		count[class_[i]] += 1
	for j in range(1, n):
		count[j] += count[j - 1]
	for i in reversed(range(n)):
		start = (order[i] - l + n) % n
		cl = class_[start]
		count[cl] -= 1
		new_order[count[cl]] = start
	return new_order

def update_classes(new_order, class_, l):
	n = len(new_order)
	new_class = [0] * n
	new_class[new_order[0]] = 0
	for i in range(1, n):
		cur = new_order[i]
		prev = new_order[i - 1]
		mid = (cur + l) % n
		mid_prev = (prev + l) % n
		if class_[cur] != class_[prev] or \
			class_[mid] != class_[mid_prev]:
			new_class[cur] = new_class[prev] + 1
		else:
			new_class[cur] = new_class[prev]
	return new_class

def build_suffix_array(s):
	n = len(s)
	order = sort_chars(s)
	class_ = compute_char_classes(s, order)
	l = 1
	while l < n:
		order = sort_doubled(s, l, order, class_)
		class_ = update_classes(order, class_, l)
		l *= 2
	return order

if __name__ == '__main__':
	s = input()
	# s = 'AACGATAGCGGTAGA$'
	print(*build_suffix_array(s))


