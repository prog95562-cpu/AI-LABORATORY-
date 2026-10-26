# Experiment 3: Hill Climbing

def hill_climbing(start, goal, graph):
    current = start
    path = [current]

    while current != goal:
        neighbors = graph.get(current, [])

        if not neighbors:
            break

        best_neighbor = max(neighbors, key=lambda x: x[1])

        if best_neighbor[1] <= 0:
            break

        current = best_neighbor[0]
        path.append(current)

    print("Path:", " -> ".join(path))
    print("Final State:", current)


graph = {
    'A': [('B', 3), ('C', 5)],
    'B': [('D', 2)],
    'C': [('D', 8), ('E', 4)],
    'D': [],
    'E': []
}

start = input("Start state: ").upper()
goal = input("Goal state: ").upper()

hill_climbing(start, goal, graph)