l = []
while True:
    a = int(input('type a number: '))
    l.append(a)
    b = input('do you want continue? ').strip().lower()[0]
    if b in 'n':
        break
print(len(l))
print(sorted(l, reverse=True))
print(l.count(5))
