import numpy as np

if __name__ == '__main__':
    with open('data', 'r') as f:
        data = f.read()
    data = [[tuple(map(int, val.strip().split(','))) for val in row.strip().split(' -> ')]  for row in data.strip().split('\n')]

    # Filter non vertical/horizontal
    data = [line for line in data if line[0][0] == line[1][0] or line[0][1] ==
            line[1][1]]

    L = 1000
    counter_matrix = [[0 for _ in range(L)] for _ in range(L)]
    for line in data:
        x_points = [line[0][0], line[1][0]]
        y_points = [line[0][1], line[1][1]]
        if x_points[0] == x_points[1]:
            for y in range(min(y_points), max(y_points) + 1):
                counter_matrix[x_points[0]][y] += 1
        else:
            for x in range(min(x_points), max(x_points) + 1):
                counter_matrix[x][y_points[0]] += 1


    result = np.array(counter_matrix)
    print(len(result[result > 1]))
            





