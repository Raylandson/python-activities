l = []
for c in range(5):
    x = int(input('type a number: '))
    l.append(x)
posh = []
posl = []
h = 0
low = 0
for c, v in enumerate(l):
    if c == 0:
        h = v
        low = v
    if v > h:
        h = v
    if v < low:
        low = v
for c in range(len(l)):
    if low == l[c]:
        posl.append(c)
    if h == l[c]:
        posh.append(c)
print(f'You has written the values {l}')
print(f'the higher value typed was {h} and your positions was: ', end='')
for a in posh:
    print(a, end='... ')
print(f'\nthe lower value typed was {low} and your positions was: ', end='')
for b in posl:
    print(b, end='... ')
# print(f'the higher is {max(l)} your position is {l.index(max(l))+1}, the lower is {min(l)} and his position is '
#       f'{l.index(min(l))+1}')
