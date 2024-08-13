# https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/

import heapq

def dijkstra(graph, start):
    # Priority queue to hold vertices to be explored
    priority_queue = []
    # Distances dictionary to store the shortest path from start to each vertex
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    # Push the start vertex into the queue with distance 0
    heapq.heappush(priority_queue, (0, start))
    
    while priority_queue:
        # Get the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If the current distance is greater than the stored distance, skip processing
        if current_distance > distances[current_vertex]:
            continue

        # Explore the neighbors of the current vertex
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # If a shorter path to neighbor is found, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)

print(f"Shortest paths from {start_vertex}: {shortest_paths}")
