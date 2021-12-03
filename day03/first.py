if __name__ == '__main__':
    with open('data', 'r') as f:
        data = f.read()
    data = [list(map(int, list(value))) for value in data.strip().split('\n')]
    
    result = ''.join([str(int(sum([row[x] for row in data])/len(data) >= 0.5))
                      for x in range(len(data[0]))])
    gamma = int(result, 2)
    epsilon = ((1 << (len(result))) - 1) ^ gamma

    print(gamma * epsilon)


