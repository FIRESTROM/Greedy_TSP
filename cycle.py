from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def have_cycle_recu(self, v, visited, parent):
        visited[v] = 1
        for i in self.graph[v]:
            if visited[i] == 0:
                if self.have_cycle_recu(i, visited, v):
                    return True
            elif parent != i:
                return True
        return False

    def have_cycle(self):
        visited = [0 for i in range(self.V)]
        for i in range(self.V):
            if visited[i] == 0:
                if self.have_cycle_recu(i, visited, -1):
                    return True
        return False
