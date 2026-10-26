# Experiment 6: Alpha-Beta Pruning

def alpha_beta(depth, node, maximizing_player, values, alpha, beta, max_depth):
    if depth == max_depth:
        return values[node]

    if maximizing_player:
        best = float('-inf')

        for i in range(2):
            value = alpha_beta(
                depth + 1,
                node * 2 + i,
                False,
                values,
                alpha,
                beta,
                max_depth
            )

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for i in range(2):
            value = alpha_beta(
                depth + 1,
                node * 2 + i,
                True,
                values,
                alpha,
                beta,
                max_depth
            )

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


values = list(map(int, input("Enter leaf values: ").split()))

max_depth = 0
n = len(values)

while (1 << max_depth) < n:
    max_depth += 1

if (1 << max_depth) != n or n < 2:
    print("Enter a power-of-two number of leaf values (minimum 2).")
else:
    result = alpha_beta(
        0,
        0,
        True,
        values,
        float('-inf'),
        float('inf'),
        max_depth
    )

    print("Optimal value:", result)