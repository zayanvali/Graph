class graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[]*n for i in range(n)]
    def create_edge(self, x, y):
        self.adj[x-1].append(y-1)
        self.adj[y-1].append(x-1)
    def bsf(self, source):
        visited = [False]*self.n
        res = []
        queue = []
        queue.append(source)
        visited[source] = True
        while len(queue) > 0:
            s = queue.pop()
            res.append(s)