# Experiment 4: A* Algorithm

def astar(graph, start, goal, heuristic):
    open_list = [(0, start)]
    came_from = {}
    g_score = {start: 0}

    while open_list:
        open_list.sort()
        _, current = open_list.pop(0)

        if current == goal:
            path = [current]

            while current in came_from:
                current = came_from[current]
                path.append(current)

            path.reverse()
            print("Path:", " -> ".join(path))
            print("Cost:", g_score[goal])
            return

        for neighbor, cost in graph.get(current, []):
            tentative_g = g_score[current] + cost

            if tentative_g < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic[neighbor]
                open_list.append((f_score, neighbor))

    print("No path found")


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 1)],
    'D': [('G', 5)],
    'E': [('G', 3)],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 4,
    'E': 2,
    'G': 0
}

start = input("Start node: ").upper()
goal = input("Goal node: ").upper()

astar(graph, start, goal, heuristic)