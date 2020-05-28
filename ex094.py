# average = média
l = []
a = 'y'
women = list()

while a != 'n':
    d = dict()
    d['name'] = input('name: ').strip()
    d['sex'] = input('sex[M/F]:').strip().lower()[0]
    d['age'] = int(input('age: '))
    print(d['name'])
    if d['sex'] in 'f':
        women.append(d.copy()['name'])
    l.append(d.copy())
    a = input('do you want continue[Y/N]? ').strip().lower()[0]

agea = 0
for v in (l):
    agea += v['age']
agea /= len(l)

print('-='*30)
print(f"- The group have {len(l)} peoples\n"
      f"- The age average is {agea}\n"
      f"- the registered women was {women}")
print(l)
