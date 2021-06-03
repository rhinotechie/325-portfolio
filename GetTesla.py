def getTesla(M):
    # Sets minimum health needed for first position.
    if grid_matrix[0][0] < 0:
        start_hp = grid_matrix[0][0] * -1 + 1
    else:
        start_hp = 1

    # Maps nodes to minimum health needed to reach that node.
    nodes = {
        (0, 0): start_hp
    }

    for y in range(0, len(grid_matrix)):
        for x in range(0, len(grid_matrix[0])):
            # Adds longest path cost coming from the left position.
            if x - 1 >= 0:
                nodes[(x, y)] = nodes[(x - 1, y)] + grid_matrix[y][x]

                # If the minimum hp would drop to 0 or less, update the minimum to reach at least 1 at this point.
                if nodes[(x, y)] <= 0:
                    nodes[(x, y)] = nodes[(x, y)] * -1 + 1

            # Adds longest path cost coming from the right position.
            if y - 1 >= 0:
                path_cost = nodes[(x, y - 1)] + grid_matrix[y][x]
                if (x, y) in nodes:
                    nodes[(x, y)] = max(path_cost, nodes[(x, y)])
                else:
                    nodes[(x, y)] = path_cost

                # If the minimum hp would drop to 0 or less, update the minimum to reach at least 1 at this point.
                if nodes[(x, y)] <= 0:
                    nodes[(x, y)] = nodes[(x, y)] * -1 + 1

    return start_hp


if __name__ == "__main__":
    grid_matrix = [[-1, -2, 2], [10, -8, 1], [-5, -2, -3]]
    print(getTesla(grid_matrix))
