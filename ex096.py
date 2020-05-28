def showline(x):
    print('-' * x)


list = [showline(5), print('123')]
showline(5)

print(list[0])
l1 = [1, 2, 3]
l2 = [2, 5, 7]


def arraymult(x, y):
    for a in x:
        print()
        for b in y:
            print(a * b, end='; ')


arraymult(l1, l2)
