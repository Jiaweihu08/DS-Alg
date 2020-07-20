def is_balanced(S):
	n = len(S)
	brackets = '( ) [ ] { }'.split()
	stack = list()

	for i in range(n):
		char = S[i]
		if char in brackets:
			if char in ('(', '[', '{'):
				stack.append((i + 1, char))
			else:
				if not stack:
					return i + 1
				top = stack.pop()[1]
				if (top == '(' and char != ')') or \
					(top == '[' and char != ']') or \
					(top == '{' and char != '}'):
					return i + 1

	output = 'Success' if not stack else stack[0][0]
	return output

if __name__ == '__main__':
	S = input()
	print(is_balanced(S))