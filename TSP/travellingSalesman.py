# def solve(graph,source,neighbours):
#     if(len(neighbours)==0):
#         return
#     else:
#         paths = []
#         for neighbour in neighbours:
#             paths.append(graph[source][neighbour]+solve(graph,neighbour,neighbours))
#             min_cost = min(paths)
#     return min_cost

# def TSP(graph, source, visited):
#    if len(visited) == len(graph):
#        return graph[source][visited[0]]
#    min_path = float('inf')
#    for neighbour in graph[source]:
#        if neighbour not in visited:
#            current_path = graph[source][neighbour] + TSP(graph, neighbour, visited | {neighbour})
#            min_path = min(min_path, current_path)
#    return min_path

def solve(graph, source, neighbours):
    if len(neighbours) == 0:
        return 0
    else:
        paths = []
        for neighbour in neighbours:
            new_neighbours = neighbours.copy()
            new_neighbours.remove(neighbour)
            paths.append(graph[source][neighbour] +
                         solve(graph, neighbour, new_neighbours))
        min_cost = min(paths)
    return min_cost


# Define the graph
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'C': 2},
    'C': {'A': 3, 'B': 2}
}

# Define the source node and its neighbors
source = 'A'
neighbours = set(['B', 'C'])

# Call the solve function
min_cost = solve(graph, source, neighbours)

print("Minimum cost:", min_cost)
