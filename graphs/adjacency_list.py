class Graph:
    def __init__(self):
        # Initialize an empty dictionary to store the adjacency list
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        # Add a vertex if it doesn't already exist
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2, bidirectional=True):
        # Add an edge between vertex1 and vertex2
        if vertex1 not in self.adjacency_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adjacency_list:
            self.add_vertex(vertex2)
        self.adjacency_list[vertex1].append(vertex2)
        if bidirectional:
            self.adjacency_list[vertex2].append(vertex1)

    def display(self):
        # Print the adjacency list
        for vertex, neighbors in self.adjacency_list.items():
            print(f"{vertex}: {neighbors}")

# Example usage:
graph = Graph()
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D", bidirectional=False)
graph.display()