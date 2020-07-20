class Solver:
    def __init__(self, k, t, p):
        self.t = t
        self.p = p
        self.k = k
        self.count = 0
        self.m1 = 10 ** 9 + 7
        self.m2 = 10 ** 9 + 9
        self.x = 99
        self.y_mod1, self.y_mod2 = self.get_pow_x()
        self.t_hashes_mod1, self.t_hashes_mod2 = self.precompute_hashes(self.t)
        self.p_hashes_mod1, self.p_hashes_mod2 = self.precompute_hashes(self.p)

    def get_pow_x(self):
        n = len(t) + 1
        pow_mod1 = [1] * n
        pow_mod2 = [1] * n
        for i in range(1, n):
            pow_mod1[i] = pow_mod1[i - 1] * self.x % self.m1
            pow_mod2[i] = pow_mod2[i - 1] * self.x % self.m2
        return pow_mod1, pow_mod2

    def precompute_hashes(self, s):
        n = len(s) + 1
        h_mod1 = [0] * n
        h_mod2 = [0] * n
        for i in range(1, n):
            h_mod1[i] = (self.x * h_mod1[i - 1] + ord(s[i - 1])) % self.m1
            h_mod2[i] = (self.x * h_mod2[i - 1] + ord(s[i - 1])) % self.m2
        return h_mod1, h_mod2

    def solve(self):
        l = len(self.p)
        pos = []
        for i in range(1, len(self.t) - l + 1):
            y_mod1 = self.y_mod1[l]
            y_mod2 = self.y_mod2[l]
            t_mod1 = (self.t_hashes_mod1[i + l] - y_mod1 * self.t_hashes_mod1[i]) % self.m1
            t_mod2 = (self.t_hashes_mod2[i + l] - y_mod2 * self.t_hashes_mod2[i]) % self.m2
            p_mod1 = (self.p_hashes_mod1[i + l] - y_mod1 * self.p_hashes_mod1[i]) % self.m1
            p_mod2 = (self.p_hashes_mod2[i + l] - y_mod2 * self.p_hashes_mod2[i]) % self.m2
            if t_mod1 == p_mod1 and t_mod2 == p_mod2:
                continue
            
        return len(pos), pos


def main():
    pass



if __name__ == '__main__':
    main()
