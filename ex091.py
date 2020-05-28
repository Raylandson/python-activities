from time import sleep
from random import randint
from operator import itemgetter

players = {'player1': randint(1, 6),
           'player2': randint(1, 6),
           'player3': randint(1, 6),
           'player4': randint(1, 6)}

print('Raffled values:')

for k, v in players.items():
    sleep(1)
    print(f"the {k} played {v}".rjust(24))

playe = dict(sorted(players.items(), key=itemgetter(1), reverse=True))

c = 1

print('the game placing is:')

for k, v in playe.items():
    sleep(1)
    print(f"{c}º is the {k} = {v}".rjust(25))
    c += 1
