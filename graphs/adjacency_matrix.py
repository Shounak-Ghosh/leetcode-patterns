def create_adjacency_matrix(V, edges):
    # Initialize an empty V x V matrix with all zeros
    matrix = [[0] * V for _ in range(V)]
    
    # Populate the matrix based on the edges
    for edge in edges:
        u, v = edge
        matrix[u][v] = 1
        matrix[v][u] = 1  # Undirected graph
    
    return matrix


# Example 1
V1 = 3
edges1 = [(0, 1), (1, 2), (2, 0)]
adj_matrix1 = create_adjacency_matrix(V1, edges1)
for row in adj_matrix1:
    print(row)
print()

# Example 2
V2 = 4
edges2 = [(0, 1), (1, 2), (1, 3), (2, 3), (3, 0)]
adj_matrix2 = create_adjacency_matrix(V2, edges2)
for row in adj_matrix2:
    print(row)