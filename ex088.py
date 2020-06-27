# games of mega sena
from random import sample
a = list(range(1, 61))
b = int(input('how many values? '))
for x in range(b):
    c = sample(a, k=6)
    c.sort()
    print(f'The {x+1}º game is {c}')
    c.clear()
