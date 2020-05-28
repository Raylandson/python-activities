# a, b, c = map(int, input().split())

a = 'y'
soccer = {}
l = list()

while a != 'n':
    soccer['name'] = input('player name: ')
    a = int(input('how many matches did he played? '))

    e = []

    for x in range(a):
        c = int(input(f'how many goals did he score in the {x+1}º match? '))
        e.append(c)

    soccer['goals'] = e[:]
    soccer['total'] = sum(e)

    l.append(soccer.copy())
    a = input('Do you want continue?').strip().lower()[0]

print('-='*30)

print(f'{"cod:<0"}'
      f'name'.ljust(1),
      f'goals'.rjust(20),
      f'total'.rjust(20))

print('--'*25)

for c, v in enumerate(l):
    print(f'{c:}'.rjust(3),
          f'{v["name"]}'.ljust(1),
          f'{v["goals"]}'.rjust(20),
          f'{sum(v["goals"])}'.rjust(20))

while True:
    rt = int(input(f'Show data of which player? '))
    if rt == 999:
        break
    elif rt >= len(l):
        print('error 404 not found')
    else:
        print(f'-- {l[rt]["name"]} data...')

        for c, v in enumerate(l[rt]['goals']):
            print(f"    in game {c} scored {v} goals.")


"""
print('-='*30)
print(soccer)
print('-='*30)

for k, v in soccer.items():
    print(f"the camp {k} has the value {v}")

print('-='*30)
print(f"the player {soccer['name']} played {len(soccer['goals'])} matches")

for c, v in enumerate(soccer['goals']):
    print(f"=> In the {c+1}º match, has score {v} goals".rjust(40))

print(f"in the total has {soccer['total']} goals")
"""
