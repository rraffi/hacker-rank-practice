if __name__ == '__main__':
    l = []
    commands = []

    for _ in range(int(input())):
        commands.append(input().split())

    for c in commands:
        if c[0] == 'append':
            l.append(int(c[1]))
        elif c[0] == 'insert':
            l.insert(int(c[1]), int(c[2]))
        elif c[0] == 'print':
            print(l)
        elif c[0] == 'sort':
            l.sort()
        elif c[0] == 'pop':
            l.pop()
        elif c[0] == 'reverse':
            l.reverse()
