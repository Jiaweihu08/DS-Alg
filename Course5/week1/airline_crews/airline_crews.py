# python3

# class Vertex:
#     def __init__(self, key):
#         self.key = key
#         self.dist = 0
#         self.prev = None
#         self.edges = []

#     def __lt__(self, other):
#         return self.dist < other.dist

#     def __eq__(self, other):
#         return self.key == other.key

# class Edge:
#     def __init__(self, u, v, capacity):
#         self.u = u
#         self.v = v
#         self.capacity = capacity

#     def relax(self):
#         if self.capacity > 0 and self.v.dist > self.u.dist + 1:
#             self.v.dist = self.u.dist + 1
#             self.v.prev = self.u
#             return True
#         return False


class MaxMatching:
    # def __init__(self):
    #     self.adj_matrix = read_data()
    #     self.num_crews = len(self.adj_matrix[0])
    #     self.num_flights = len(self.adj_matrix)
    #     self.graph = [Vertex(i) for i in range(self.num_crews + self.num_flights + 2)]
    #     s = self.graph[0]
    #     s.dist = 0
    #     s.edges.extend([Edge(s, self.graph[i], 1) for i in range(
    #         1 + self.num_crews,
    #         1 + self.num_crews + self.num_flights)])
    #     t = self.graph[-1]
    #     t.edges.extend([Edge(self.graph[j], t, 1) for j in range(
    #         1,
    #         1 + self.num_crews)])
    #     for i in range(self.num_flights):
    #         for j in range(self.num_crews):
    #             if self.adj_matrix[i][j] == 1:
    #                 v = i + 1 + self.num_crews
    #                 u = j + 1
    #                 forward_edge = Edge(self.graph[u], self.graph[v], 1)
    #                 backward_edge = Edge(self.graph[v], self.graph[u], 0)
    #                 self.graph[]

    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def find_matching(self, adj_matrix):
        # Replace this code with an algorithm that finds the maximum
        # matching correctly in all cases.
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        matching = [-1] * n
        busy_right = [False] * m
        for i in range(n):
            for j in range(m):
                if adj_matrix[i][j] and matching[i] == -1 and (not busy_right[j]):
                    matching[i] = j
                    busy_right[j] = True
        return matching


    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)

if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
