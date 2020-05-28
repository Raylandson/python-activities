everybody = []
people = []
while True:
    people.append(input('Name: '))
    people.append(float(input('weight: ')))
    everybody.append(people[:])
    people.clear()
    a = input('Do you want continue?[y/n]: ').lower().strip()[0]
    if a == 'n':
        break
hiw = low = 0
mostw = []
lowsw = []
for x, w in enumerate(everybody):
    if x == 0:
        hiw = w[1]
        low = w[1]
    if w[1] > hiw:
        hiw = w[1]
    elif w[1] < low:
        low = w[1]
for p in everybody:
    if p[1] == hiw:
        mostw.append(p[0])
    elif p[1] == low:
        lowsw.append(p[0])
print(f'you registered {len(everybody)} peoples\n'
      f'the higher weight was {hiw}, the weight of {mostw}\n'
      f'the lowest weight was {low}, the weight of {lowsw}\n')
