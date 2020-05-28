l = []
odd = []
even = []
while True:
    a = int(input('type a number: '))
    l.append(a)
    if a % 2 == 0:
        odd.append(a)
    else:
        even.append(a)
    b = input('do you want continue? ').strip().lower()[0]
    if b in 'n':
        break
print(l)
print(odd)
print(even)
