
# Task 2: UCS
import heapq

graph = {
    "A": [("B", 1), ("C", 2)],
    "B": [("D", 8), ("E", 1)],
    "C": [("F", 4), ("G", 10)],
    "D": [],
    "E": [("G", 1)],
    "F": [],
    "G": []
}
def ucs(start, goal):
    queue = [(0, start, [start])]
    visited = []
    while queue:
        cost, node, path = heapq.heappop(queue)
        if node in visited:
            continue

        visited.append(node)
        print("Processing:", node, "Cost:", cost)
        if node == goal:
            print("Path:", path)
            print("Total cost:", cost)
            print("Visit order:", visited)
            return
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    queue,
                    (cost + weight, neighbor, path + [neighbor])
                )
    print("Goal not found")

ucs("A", "G")
