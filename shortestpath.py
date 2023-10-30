import heapq
import math
from graphObject import districts


def shortest_path(graph, start, end):
    heap = [(0, start)]
    visited = set()
    while heap:
        (cost, node) = heapq.heappop(heap)
        if node not in visited:
            visited.add(node)
            if node == end:
                path = []
                while node in predecessors:
                    path.append(node)
                    node = predecessors[node]
                path.append(start)
                return path[::-1], cost
            for (neighbor, c) in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + c, neighbor))
                    predecessors[neighbor] = node
    return [], math.inf


predecessors = {}
# you can replace the district name with any name imported from graphObject
path, path_cost = shortest_path(districts, "Mchinji", "Ntcheu")
if not path:
    print("There is no path between Mchinji and Ntcheu.")
else:
    print(
        f"The shortest path from Mchinji to Ntcheu is {path} with a total distance of {path_cost} km.")
