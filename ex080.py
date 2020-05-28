l = []
for a in range(5):
    b = int(input('type a value: '))
    if a == 0 or b >= max(l):
        l.append(b)
        print('was append in the end of list')
    elif b <= min(l):
        l.insert(0, b)
        print('was append in the early of list')
    else:
        for c in range(0, len(l)):
            if l[c] < b <= l[c+1]:
                l.insert(c+1, b)
                print('was append in the middle of list')
                break
print(l)
