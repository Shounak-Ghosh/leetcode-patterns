def bellman_ford(graph, start):
    # Initialize distances from start to all vertices as infinity
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Relax edges up to |V| - 1 times
    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex]:
                if distances[vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[vertex] + weight

    # Check for negative-weight cycles
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            if distances[vertex] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative-weight cycle")

    return distances

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': [('B', -10)]  # Example with negative weight
}

start_vertex = 'A'
try:
    shortest_paths = bellman_ford(graph, start_vertex)
    print(f"Shortest paths from {start_vertex}: {shortest_paths}")
except ValueError as e:
    print(e)
