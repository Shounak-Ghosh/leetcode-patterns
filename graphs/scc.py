from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack=None):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited, stack)
        if stack is not None:
            stack.append(v)

    def transpose(self):
        g = Graph(self.vertices)
        for u in self.graph:
            for v in self.graph[u]:
                g.graph[v].append(u)
        return g

    def fill_order(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.fill_order(i, visited, stack)
        stack.append(v)

    def count_scc(self):
        stack = []
        visited = [False] * self.vertices

        # Fill vertices in stack according to their finishing times
        for i in range(self.vertices):
            if not visited[i]:
                self.fill_order(i, visited, stack)

        # Create a reversed graph
        gr = self.transpose()

        # Mark all the vertices as not visited (For second DFS)
        visited = [False] * self.vertices

        # Now process all vertices in the order defined by the stack
        scc_count = 0
        while stack:
            i = stack.pop()
            if not visited[i]:
                gr.dfs(i, visited)
                scc_count += 1

        return scc_count

# Example usage:
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    print("Number of Strongly Connected Components:", g.count_scc())
