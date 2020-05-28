# games of mega sena
from random import sample
a = list(range(1, 11))
b = int(input('how many values? '))
for x in range(b):
    c = sample(a, k=3)
    c.sort()
    print(f'The {x+1}º game is {c}')
    c.clear()
