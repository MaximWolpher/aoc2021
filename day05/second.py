import numpy as np


def make_range(x_p, y_p):
    if x_p[0] == x_p[1]:
        rang = [(x_p[0], y) for y in range(min(y_p), max(y_p) + 1)]
    elif y_p[0] == y_p[1]:
        rang = [(x, y_p[0]) for x in range(min(x_p), max(x_p) + 1)]
    else:
        if x_p[0] > x_p[1]:
            x_range = list(range(min(x_p), max(x_p) + 1))[::-1]
        else:
            x_range = list(range(min(x_p), max(x_p) + 1))
        if y_p[0] > y_p[1]:
            y_range = list(range(min(y_p), max(y_p) + 1))[::-1]
        else:
            y_range = list(range(min(y_p), max(y_p) + 1))

        rang = list(zip(x_range, y_range))
    return rang
        


if __name__ == '__main__':
    with open('data', 'r') as f:
        data = f.read()
    data = [[tuple(map(int, val.strip().split(','))) for val in row.strip().split(' -> ')]  for row in data.strip().split('\n')]

    # Filter non vertical/horizontal
    L = 1000
    counter_matrix = [[0 for _ in range(L)] for _ in range(L)]
    for line in data:
        x_points = [line[0][0], line[1][0]]
        y_points = [line[0][1], line[1][1]]
        rang = make_range(x_points, y_points)
        for x, y in rang:
            counter_matrix[x][y] += 1


    result = np.array(counter_matrix)
    print(len(result[result > 1]))
            





