a = [[[], [], []], [[], [], []], [[], [], []]]
for b, c in enumerate(a):
    for d, e in enumerate(a[b]):
        x = int(input(f'which value in {b}, {d}: '))
        a[b][d].append(x)
for b, c in enumerate(a):
    for d, e in enumerate(a[b]):
        print(f'[{e[0]:^5}]'.center(5), end='')
    print()
