with open('data', 'r') as f:
    data = f.read()
data = [int(value) for value in data.strip().split('\n')]

result = sum([data[idx + 1] > data[idx] for idx in range(len(data) - 1)])
print(result)
