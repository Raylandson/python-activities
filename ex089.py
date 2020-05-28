allstudents = []
while True:
    gr = []
    student = list()
    s = input('Name: ')
    gr.append(float(input('grade 1: ')))
    gr.append(float(input('grade 2: ')))
    student.append(s)
    student.append(gr[:])
    allstudents.append(student[:])
    a = input('do you want continue?[y/n]: ').strip().lower()[0]

    if a == 'n':
        break

print('<-'*20)
print(f'{"Num":<10} {"Name":<10} {"Average":<10}')

for y, x in enumerate(allstudents):
    print(f' {y:<10} {x[0]:<10} {(x[1][0] + x[1][1])/2:<10.1f}')
while True:
    a = int(input('show grades for which student?(999 break) '))
    if a == 999:
        break
    if a >= len(allstudents):
        print('out of range, please type again...')
    else:
        print(f'the grades of {allstudents[a][0]} are {allstudents[a][1]}')
