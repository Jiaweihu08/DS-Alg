class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, dst, src):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return
        
        total_rows = self.row_counts[dst_parent] + self.row_counts[src_parent]
        
        if self.ranks[dst_parent] >= self.ranks[src_parent]:
            self.parents[src_parent] = dst_parent
            self.row_counts[dst_parent] = total_rows
            self.row_counts[src_parent] = 0
            if self.ranks[dst_parent] == self.ranks[src_parent]:
                self.ranks[dst_parent] += 1
        else:
            self.parents[dst_parent] = src_parent
            self.row_counts[src_parent] = total_rows
            self.row_counts[dst_parent] = 0

        if total_rows > self.max_row_count:
            self.max_row_count = total_rows


    def get_parent(self, table):
            if self.parents[table] != table:
                self.parents[table] = self.get_parent(self.parents[table])
            return self.parents[table]


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables

    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)

    # n_tables, n_queries = 5, 5
    # counts = [1] * 5
    # db = Database(counts)
    # queries = [(3,5),(2,4),(1,4),(5,4),(5,3)]
    
    # queries = []
    # with open('116.txt') as f:
    #     n, m = list(map(int, f.readline().split()))
    #     row_counts = list(map(int, f.readline().split()))
    #     for _ in range(m):
    #         queries.append(tuple(map(int, f.readline().split())))

    # answers = []
    # with open('116a.txt') as f:
    #     for _ in range(m):
    #         answers.append(int(f.readline()))

    # out = []
    # db = Database(row_counts.copy())
    # for dst, src in queries:
    #      db.merge(dst - 1, src - 1)
    #      out.append(db.max_row_count)
    #      # print(db.max_row_count)

    # print('All worked out?', out == answers)


if __name__ == "__main__":
    main()






