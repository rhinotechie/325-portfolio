import sys


def getTesla(M):
    nodes = {}  # Maps nodes to current path health and minimum health needed to get there

    # Sets minimum health needed for first position.
    if M[0][0] <= 0:
        nodes[(0, 0)] = [1, M[0][0] * -1 + 1]
    else:
        nodes[(0, 0)] = [M[0][0] + 1, 1]

    for y in range(0, len(M)):
        for x in range(0, len(M[0])):
            # If available, forms a path from the left side by default.
            if x - 1 >= 0:
                nodes[(x, y)] = [nodes[(x - 1, y)][0] + M[y][x], nodes[(x - 1, y)][1]]

                # If the minimum hp would drop to 0 or less, the minimal health is increased to survive and the path
                # cost is set to the lowest surviving value.
                if nodes[(x, y)][0] <= 0:
                    nodes[(x, y)][1] += nodes[(x, y)][0] * -1 + 1
                    nodes[(x, y)][0] = 1

            # If available, forms a path from the top if this path results in a lower minimal health value.
            if y - 1 >= 0:
                if (x, y) in nodes:
                    if nodes[(x, y - 1)][1] < nodes[(x, y)][1]:
                        nodes[(x, y)] = [nodes[(x, y - 1)][0] + M[y][x], nodes[(x, y - 1)][1]]
                    elif nodes[(x, y - 1)][1] == nodes[(x, y)][1] and nodes[(x, y - 1)][0] > nodes[(x, y)][0]:
                        nodes[(x, y)] = [nodes[(x, y - 1)][0] + M[y][x], nodes[(x, y - 1)][1]]
                else:
                    # Defaults to top path if no other path.
                    nodes[(x, y)] = [nodes[(x, y - 1)][0] + M[y][x], nodes[(x, y - 1)][1]]

                # If the minimum hp would drop to 0 or less, the minimal health is increased to survive and the path
                # cost is set to the lowest surviving value.
                if nodes[(x, y)][0] <= 0:
                    nodes[(x, y)][1] += nodes[(x, y)][0] * -1 + 1
                    nodes[(x, y)][0] = 1

    return nodes[(len(M[0]) - 1, len(M) - 1)][1]


def getTesla2(M):
    minimum_hp = sys.maxsize
    node_stack = [(0, 0)]
    cost_stack = []
    minimum_stack = []
    nodes = {}

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
        if node_stack[-1][0] + 1 < len(M[0]):
            # Updates eastern node's path cost coming from this node.
            cost_stack.append(cost_stack[-1] + M[node_stack[-1][1]][node_stack[-1][0] + 1])
            if cost_stack[-1] <= 0:
                minimum_stack.append(minimum_stack[-1] + cost_stack[-1] * -1 + 1)
                cost_stack[-1] = 1
            else:
                minimum_stack.append(minimum_stack[-1])

            node_stack.append((node_stack[-1][0] + 1, node_stack[-1][1]))
            continue

        # Southern node
        if node_stack[-1][1] + 1 < len(M):
            # Updates southern node's path cost coming from this node.
            cost_stack.append(cost_stack[-1] + M[node_stack[-1][1] + 1][node_stack[-1][0]])
            if cost_stack[-1] <= 0:
                minimum_stack.append(minimum_stack[-1] + cost_stack[-1] * -1 + 1)
                cost_stack[-1] = 1
            else:
                minimum_stack.append(minimum_stack[-1])

            node_stack.append((node_stack[-1][0], node_stack[-1][1] + 1))
            continue

        # If this is a full path to the end that has the lowest minimal hp so far, update the minimum hp.
        if node_stack[-1][0] == len(M[0]) - 1 and node_stack[-1][1] == len(M) - 1 and \
                minimum_stack[-1] < minimum_hp:
            minimum_hp = minimum_stack[-1]

        node_stack.pop()
        minimum_stack.pop()
        cost_stack.pop()

    return minimum_hp


if __name__ == "__main__":
    grid_matrix = [[-1, -2, 2], [10, -8, 1], [-5, -2, -3]]
    print(getTesla2(grid_matrix))
