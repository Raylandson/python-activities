# odd = ímpar
# even/pair = par

a = [[[], [], []], [[], [], []], [[], [], []]]
evensum = 0
for b, c in enumerate(a):
    for d, e in enumerate(a[b]):
        x = int(input(f'which value in {b}, {d}: '))
        a[b][d].append(x)
        if x % 2 == 0:
            evensum += x
for b, c in enumerate(a):
    for d, e in enumerate(a[b]):
        print(f'[{e[0]:^5}]'.center(5), end='')
    print()
print(f'the sum of every even is {evensum}')
print(f'the sum  of the third column is {a[0][2][0] + a[1][2][0] + a[2][2][0]}')
hi = 0
for b, c in enumerate(a[1]):
    if b == 0:
        hi = a[1][b]
    elif c > hi:
        hi = a[1][b]
print(f'the highest value of the second line is {hi[0]}')
