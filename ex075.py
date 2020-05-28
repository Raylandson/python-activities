a = (int(input('choice a number: ')), int(input('choice a number: ')), int(input('choice a number: ')),
     int(input('choice a number: ')))
print(f'the number nine has happen {a.count(9)} times')
print(f'the value three has happen in the position {a.index(3) + 1}')
print('the even numbers is: ', end='')
for b in a:
    if b % 2 == 0:
        print(f'{b}', end=' ')
