# hiring = contratação
# retirement = aposentadoria

people = dict()
people['name'] = input('your name: ')
datbir = int(input('date of birth: '))
people['age'] = 2020 - datbir
people['ctps'] = int(input('your ctps (0 = not have): '))

if people['ctps'] != 0:
    people['hiring'] = int(input('the date of your hiring: '))
    people['salary'] = float(input('your salary: '))
    people['retirement'] = (people['hiring'] - datbir) + 35
print()
print(people)
print()
for k, v in people.items():
    print(f"{k} have the value {v}")
