import heapq
from prettytable import PrettyTable

def dijkstra_shortest_path(graph, source):
    # Initialize distance from source to all vertices as infinity
    distances = {v: float('inf') for v in graph}
    distances[source] = 0

    # Initialize priority queue
    pq = [(0, source)]

    # Initialize shortest paths tree
    shortest_paths = {source: None}

    # Loop until priority queue is empty
    while pq:
        # Get vertex with smallest distance from priority queue
        (dist, current_vertex) = heapq.heappop(pq)

        # Ignore vertex if it has already been visited
        if dist > distances[current_vertex]:
            continue

        # Explore all neighboring vertices
        for neighbor, weight in graph[current_vertex].items():
            distance = dist + weight

            # If a shorter path to the neighbor is found, update distances and shortest paths tree
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_paths[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    # Display shortest path directions from source to all vertices in a table
    table = PrettyTable()
    table.field_names = ["Destination", "Shortest Path Directions"]
    for v in graph:
        if shortest_paths[v] is None:
            table.add_row([v, None])
        else:
            path = []
            current_vertex = v
            while current_vertex != source:
                path.insert(0, current_vertex)
                current_vertex = shortest_paths[current_vertex]
            path.insert(0, source)
            table.add_row([v, " -> ".join(str(p) for p in path)])
    print(table)

# Driver code to read input file and call Dijkstra's algorithm
files = ['tinyDG.txt', 'mediumDG.txt','largeDG.txt' ]

for file in files:
    with open(file, 'r') as f:
        num_vertices = int(f.readline())
        num_edges = int(f.readline())

        graph = {i: {} for i in range(num_vertices)}
        for line in f:
            v1, v2, weight = map(float, line.strip().split())
            graph[int(v1)][int(v2)] = weight

        dijkstra_shortest_path(graph, 0)