allnumbers = [[], []]
for a in range(7):
    b = int(input(f'type the {a+1}º value: '))
    if b % 2 == 0:
        allnumbers[0].append(b)
    else:
        allnumbers[1].append(b)
allnumbers[0].sort()
allnumbers[1].sort()
print(f'The even values was {allnumbers[0]}\n'
      f'The odd values was {allnumbers[1]}')
