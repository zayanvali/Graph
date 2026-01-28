class graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[]for i in range (V)]
    def dfs_util(self, temp, v, visited):
        visited[v] = True
        temp.append(v)
        for i in self.adj[v]:
            if visited[i] == False:
                temp = self.dfs_util(temp, i, visited)
        return temp
    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
    def connected_components(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                cc.append(self.dfs_util(temp, v, visited))
if __name__ == "__main__":
    g = graph(5)
    g.add_edge(1, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    print(g)
    cc = g.connected_components()
    print(cc)