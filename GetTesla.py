def getTesla(M):
    nodes = {
        (0, 0): grid_matrix[0][0]
    }
    if grid_matrix[0][0] < 0:
        start_hp = grid_matrix[0][0] * -1 + 1
    else:
        start_hp = 1

    for y in range(0, len(grid_matrix)):
        for x in range(0, len(grid_matrix[0])):
            # Adds longest path cost coming from the left position.
            if x - 1 >= 0:
                nodes[(x, y)] = nodes[(x - 1, y)] + grid_matrix[y][x]

            # Adds longest path cost coming from the right position.
            if y - 1 >= 0:
                new_val = nodes[(x, y - 1)] + grid_matrix[y][x]
                if (x, y) in nodes:
                    nodes[(x, y)] = max(new_val, nodes[(x, y)])
                else:
                    nodes[(x, y)] = new_val

    return start_hp


if __name__ == "__main__":
    #grid_matrix = [[-1, -2, 2], [10, -8, 1], [-5, -2, -3]]
    grid_matrix = [[-5]]
    print(getTesla(grid_matrix))
