# A simple game tree where leaf nodes have scores.
# 'A' is the root, its children are 'B' and 'C'.
# 'B' and 'C' are minimizing nodes.
# 'D', 'E', 'F' and 'G' are maximizing nodes.

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [3, 5],
    'E': [2, 1],
    'F': [2, 8],
    'G': [4, 9]
}


def minimax_alpha_beta(node, depth, alpha, beta, max_player):

    # Base case: if we are at a leaf node, return the score.
    if depth == 0:
        if node in tree:
            # For this simple tree, the children are the scores.
            return tree[node][0] if max_player else tree[node][0]
        else:
            return node

    # Recursive case:

    # Maximizing player's turn (MAX)
    if max_player:
        value = float('-inf')

        for child in tree[node]:
            # Recursively call the function for the child node.
            value = max(value, minimax_alpha_beta(
                child, depth - 1, alpha, beta, False))

            alpha = max(alpha, value)

            if alpha >= beta:
                print(f"Pruning branch at node {node}")
                break  # Prune the branch

        return value

    # Minimizing player's turn (MIN)
    else:
        value = float('inf')

        for child in tree[node]:
            # Recursively call the function for the child node.
            value = min(value, minimax_alpha_beta(
                child, depth - 1, alpha, beta, True))

            beta = min(beta, value)

            if beta <= alpha:
                print(f"Pruning branch at node {node}")
                break  # Prune the branch

        return value


# Start the search from the root node 'A'.
best_score = minimax_alpha_beta(
    'A', 3, float('-inf'), float('inf'), True
)

print(f"The best score is: {best_score}")
