import sys


def getTesla(M):
    minimum_hp = sys.maxsize  # Lowest health required to keep Mr. X alive.
    node_stack = [(0, 0)]  # Nodes being processed in path
    cost_stack = []  # Costs of each node in the current path
    minimum_stack = []  # Minimum costs to reach each node in the current path
    neighbors = {}  # Prevents revisiting same path after popping items off the stack

    # Sets minimum health needed for first position.
    if M[0][0] <= 0:
        minimum_stack.append(M[0][0] * -1 + 1)
        cost_stack.append(1)
    else:
        minimum_stack.append(1)
        cost_stack.append(M[0][0] + 1)

    # Uses a stack to iterate over every possible path while preserving the lowest possible health required.
    while len(node_stack) > 0:
        # Eastern node
        if node_stack[-1][0] + 1 < len(M[0]) and (node_stack[-1][0] + 1, node_stack[-1][1]) not in neighbors:
            # Updates eastern node's path cost coming from this node.
            cost_stack.append(cost_stack[-1] + M[node_stack[-1][1]][node_stack[-1][0] + 1])
            if cost_stack[-1] <= 0:
                minimum_stack.append(minimum_stack[-1] + cost_stack[-1] * -1 + 1)
                cost_stack[-1] = 1
            else:
                minimum_stack.append(minimum_stack[-1])

            neighbors[(node_stack[-1][0] + 1, node_stack[-1][1])] = True
            node_stack.append((node_stack[-1][0] + 1, node_stack[-1][1]))
            continue

        # Southern node
        if node_stack[-1][1] + 1 < len(M) and (node_stack[-1][0], node_stack[-1][1] + 1) not in neighbors:
            # Updates southern node's path cost coming from this node.
            cost_stack.append(cost_stack[-1] + M[node_stack[-1][1] + 1][node_stack[-1][0]])
            if cost_stack[-1] <= 0:
                minimum_stack.append(minimum_stack[-1] + cost_stack[-1] * -1 + 1)
                cost_stack[-1] = 1
            else:
                minimum_stack.append(minimum_stack[-1])

            neighbors[(node_stack[-1][0], node_stack[-1][1] + 1)] = True
            node_stack.append((node_stack[-1][0], node_stack[-1][1] + 1))
            continue

        # If this is a full path to the end that has the lowest minimal hp so far, update the minimum hp.
        if node_stack[-1][0] == len(M[0]) - 1 and node_stack[-1][1] == len(M) - 1 and \
                minimum_stack[-1] < minimum_hp:
            minimum_hp = minimum_stack[-1]

        # Jumps to the previous node and its values.
        neighbors.pop((node_stack[-1][0] + 1, node_stack[-1][1]), None)
        neighbors.pop((node_stack[-1][0], node_stack[-1][1] + 1), None)
        node_stack.pop()
        minimum_stack.pop()
        cost_stack.pop()

    return minimum_hp


if __name__ == "__main__":
    grid_matrix = [[-1, -2, 2], [10, -8, 1], [-5, -2, -3]]
    print(getTesla(grid_matrix))
