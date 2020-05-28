a = ('pencil', 1.75, 'rubber', 2, 'notebook', 15.9, 'case', 25, 'transfer', 4.2, 'compass', 9.99, 'bag', 120.32, 'pens',
     22.3, 'book', 34.9)
print('-' * 31)
print(f'{"PRICE LIST":^31}')
print('-' * 31)
for x in range(0, 18, 2):
    print(f'{a[x]:.<20}',
          f'US '.ljust(0),
          f'{a[x+1]:.2f}'.rjust(6))
print('-'*31)
