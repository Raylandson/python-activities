l = []
while True:
    a = int(input('type a number: '))
    if a not in l:
        print('the value was append with success.')
        l.append(a)
    else:
        print('Ops, duplicated value, i dont will append.')
    b = input('do you want to continue? [S/N]: ').strip().lower()[0]
    if b in 'n':
        break
print(f'you typed the values {sorted(l)}')
