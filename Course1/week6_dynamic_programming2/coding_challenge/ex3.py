def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    n = len(dataset[::2])
    ops = dataset[1::2]

    M = [[None] * n for _ in range(n)]
    m = [[None] * n for _ in range(n)]
    for i in range(n):
        m[i][i] = M[i][i] = int(dataset[i * 2])

    for s in range(1, n):
        for i in range(0, n - s):
            j = i + s
            min_, max_ = float('inf'), float('-inf')
            for k in range(i, j):
                a = evalt(M[i][k], M[k + 1][j], ops[k])
                b = evalt(M[i][k], m[k + 1][j], ops[k])
                c = evalt(m[i][k], M[k + 1][j], ops[k])
                d = evalt(m[i][k], m[k + 1][j], ops[k])
                min_ = min(min_, a, b, c, d)
                max_ = max(max_, a, b, c, d)
            m[i][j], M[i][j] = min_, max_
    return M[0][-1]

if __name__ == '__main__':
    dataset = input()
    # dataset = '5-8+7*4-8+9'
    # dataset = '1+5'
    print(get_maximum_value(dataset))



