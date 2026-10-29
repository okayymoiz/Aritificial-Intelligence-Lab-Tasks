
# Task 2: DLS 

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

def dls(node, goal, limit, path):

    if node == goal:
        return "Found", path

    if limit == 0:
        if graph[node]:
            return "Cutoff", path
        else:
            return "Failure", None

    cutoff_occurred = False

    for neighbour in graph[node]:
        status, result = dls(
            neighbour, goal, limit - 1, path + [neighbour]
        )

        if status == "Found":
            return "Found", result

        if status == "Cutoff":
            cutoff_occurred = True

    if cutoff_occurred:
        return "Cutoff", path
    else:
        return "Failure", None


for limit in range(1, 5):
    status, result = dls("A", "G", limit, ["A"])
    print("Limit:", limit)
    print("Status:", status)
    print("Path:", result)
    print()

#    IDDFS

def iddfs(start, goal, max_depth):
    for limit in range(max_depth + 1):
        status, path = dls(start, goal, limit, [start])

        print("Depth:", limit, "| Status:", status)

        if status == "FOUND":
            print("Path:", path)
            return path
    return None


print("IDDFS with maximum depth 1")
iddfs("A", "G", 1)

print("\nIDDFS with maximum depth 2")
iddfs("A", "G", 2)

print("\nIDDFS with maximum depth 3")
iddfs("A", "G", 3)

print("\nIDDFS with maximum depth 4")
iddfs("A", "G", 4)