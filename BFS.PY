# Experiment 1: Breadth-First Search (BFS)

def bfs(graph, start):
    visited = [start]
    queue = [start]

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for x in graph.get(node, []):
            if x not in visited:
                visited.append(x)
                queue.append(x)


n = int(input("Vertices: "))
graph = {}

for i in range(n):
    graph[i] = list(map(int, input(f"{i}: ").split()))

start = int(input("Start: "))

print("BFS:")
bfs(graph, start)