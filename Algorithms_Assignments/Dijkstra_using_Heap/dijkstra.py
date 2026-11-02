import heapq

NETWORK = {
    "A": [("B", 4), ("C", 2)], "B": [("A", 4), ("C", 1), ("D", 5)],
    "C": [("A", 2), ("B", 1), ("D", 8)], "D": [("B", 5), ("C", 8)]
}

def shortest_paths(graph, source):
    if source not in graph:
        raise KeyError(f"Unknown source vertex: {source}")
    distance = {vertex: float("inf") for vertex in graph}
    previous = {vertex: None for vertex in graph}
    distance[source] = 0
    queue = [(0, source)]
    while queue:
        cost, vertex = heapq.heappop(queue)
        if cost > distance[vertex]:
            continue
        for neighbor, weight in graph[vertex]:
            if weight < 0:
                raise ValueError("Dijkstra cannot process negative edges")
            candidate = cost + weight
            if candidate < distance[neighbor]:
                distance[neighbor] = candidate
                previous[neighbor] = vertex
                heapq.heappush(queue, (candidate, neighbor))
    return distance, previous

def restore_path(previous, target):
    route = []
    while target is not None:
        route.append(target)
        target = previous[target]
    return list(reversed(route))

if __name__ == "__main__":
    distances, parents = shortest_paths(NETWORK, "A")
    for node, value in distances.items():
        print(f"A -> {node}: {value}; path: {' -> '.join(restore_path(parents, node))}")
