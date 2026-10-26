# Experiment 2: Depth-First Search (DFS)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    visited.append(start)
    print(start, end=" ")

    for x in graph.get(start, []):
        if x not in visited:
            dfs(graph, x, visited)


n = int(input("Vertices: "))
graph = {}

for i in range(n):
    graph[i] = list(map(int, input(f"{i}: ").split()))

start = int(input("Start: "))

print("DFS:")
dfs(graph, start)