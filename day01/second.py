with open('data', 'r') as f:
    data = f.read()
data = [int(value) for value in data.strip().split('\n')]

windows = [data[idx: idx + 3] for idx in range(len(data) - 2)]

result = sum([sum(windows[idx + 1]) > sum(windows[idx]) for idx in
              range(len(windows) - 1)])
print(result)
