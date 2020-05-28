a = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
     'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
x = int(input('write a number from zero to twenty: '))
while 0 > x or x > 20:
    x = int(input('try again. write a number from zero to twenty: '))
print(f'your extensive number is {a[x]}')
