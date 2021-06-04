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
                else:
                    # Defaults to top path if no other path.
                    nodes[(x, y)] = [nodes[(x, y - 1)][0] + M[y][x], nodes[(x, y - 1)][1]]

                # If the minimum hp would drop to 0 or less, the minimal health is increased to survive and the path
                # cost is set to the lowest surviving value.
                if nodes[(x, y)][0] <= 0:
                    nodes[(x, y)][1] += nodes[(x, y)][0] * -1 + 1
                    nodes[(x, y)][0] = 1

    return nodes[(len(M[0]) - 1, len(M) - 1)][1]


if __name__ == "__main__":
    grid_matrix = [[-1, -2, 2], [10, -8, 1], [-5, -2, -3]]
    print(getTesla(grid_matrix))
