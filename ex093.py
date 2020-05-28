soccer = {}
soccer['name'] = input('player name: ')

a = int(input('how many matches did he played? '))

e = []

for x in range(a):
    c = int(input(f'how many goals did he score in the {x+1}º match? '))
    e.append(c)

soccer['goals'] = e[:]
soccer['total'] = sum(e)

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

