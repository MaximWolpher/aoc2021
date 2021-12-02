class Submarine:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0

    def move(self, command: str, value: int):
        if command == 'forward':
            self.horizontal += value
        elif command == 'down':
            self.depth += value
        elif command == 'up':
            self.depth -= value

if __name__ == '__main__':
    with open('data', 'r') as f:
        data = f.read()
    data = [value for value in data.strip().split('\n')]
    
    
    sub = Submarine()
    for row in data:
        command, value = row.split(' ')
        sub.move(command, int(value))

    print(sub.horizontal * sub.depth)
