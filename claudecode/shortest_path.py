import heapq

def dijkstra(graph, start, end):
    """
    Calculates the shortest path between two nodes in a graph using Dijkstra's algorithm.

    Args:
        graph: A dictionary representing the graph as an adjacency list.
               The keys are the nodes, and the values are dictionaries
               of neighboring nodes and the weight of the edge.
               Example: {'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'C': 2, 'D': 5}, ...}
        start: The starting node.
        end: The ending node.

    Returns:
        A tuple containing:
            - A list of nodes representing the shortest path from start to end.
            - The total distance of the shortest path.
        If no path is found, returns (None, float('inf')).
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        if current_node == end:
            break

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    path = []
    current_node = end
    while current_node is not None:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]

    if distances[end] == float('inf'):
        return None, float('inf')
    else:
        return path, distances[end]

if __name__ == '__main__':
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
