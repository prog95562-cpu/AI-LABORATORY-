# Experiment 8: Water Jug Problem Using BFS

from collections import deque


def water_jug(capacity1, capacity2, target):
    start = (0, 0)
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (jug1, jug2), path = queue.popleft()

        if jug1 == target or jug2 == target:
            print("Solution Path:")
            for state in path:
                print(state)
            print("Target achieved!")
            return

        next_states = [
            (capacity1, jug2),
            (jug1, capacity2),
            (0, jug2),
            (jug1, 0),
            (
                jug1 - min(jug1, capacity2 - jug2),
                jug2 + min(jug1, capacity2 - jug2)
            ),
            (
                jug1 + min(jug2, capacity1 - jug1),
                jug2 - min(jug2, capacity1 - jug1)
            )
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))

    print("No solution exists.")


capacity1 = int(input("Enter capacity of Jug 1: "))
capacity2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

if target < 0 or target > max(capacity1, capacity2):
    print("Target cannot be achieved.")
else:
    water_jug(capacity1, capacity2, target)