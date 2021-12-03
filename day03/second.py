def find_common(data: list, most_common: bool, column: int) -> int:
    result = sum([row[column] for row in data]) / len(data)
    if most_common:
        return int(result >= 0.5)
    else:
        return int(result < 0.5)

def get_rating(data, oxygen: bool):
    rating = data[:]
    column = 0
    while len(rating) > 1:
        common = find_common(rating, oxygen, column)
        rating = [row for row in rating if row[column] == common]
        column += 1
    return ''.join(list(map(str, rating[0])))

if __name__ == '__main__':
    with open('data', 'r') as f:
        data = f.read()
    data = [list(map(int, list(value))) for value in data.strip().split('\n')]
   
    oxygen = get_rating(data, oxygen=True)
    scrubber = get_rating(data, oxygen=False)

    print(int(oxygen, 2) * int(scrubber, 2))

