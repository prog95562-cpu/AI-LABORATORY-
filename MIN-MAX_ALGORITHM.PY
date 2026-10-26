# Experiment 5: Minimax Algorithm

def minimax(depth, node, maximizing_player, values, max_depth):
    if depth == max_depth:
        return values[node]

    if maximizing_player:
        best = float('-inf')

        for i in range(2):
            value = minimax(depth + 1, node * 2 + i,
                            False, values, max_depth)
            best = max(best, value)

        return best

    else:
        best = float('inf')

        for i in range(2):
            value = minimax(depth + 1, node * 2 + i,
                            True, values, max_depth)
            best = min(best, value)

        return best


values = list(map(int, input("Enter leaf values: ").split()))
max_depth = 0
n = len(values)

while (1 << max_depth) < n:
    max_depth += 1

if (1 << max_depth) != n:
    print("Enter a power-of-two number of leaf values.")
else:
    result = minimax(0, 0, True, values, max_depth)
    print("Optimal value:", result)