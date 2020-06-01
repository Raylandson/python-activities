from urllib.request import urlretrieve
from os import remove, stat

x, y = map(int, input('what is the chapter range? ').split())
for a in range(x - 1, y):
    c = 1
    while True:
        urlretrieve(f'https://mangassuki.xyz/sys_mangas/00sdfrw/O/one-piece/cap-{a+1}/{c:04}.jpg', f'cap-{a+1}_{c}.jpg')
        # https://mangassuki.xyz/sys_mangas/00sdfrw/O/one-piece/cap-1/0001.jpg
        print(f'https://mangassuki.xyz/sys_mangas/00sdfrw/O/one-piece/cap-{a+1}/{c:04}.jpg -- cap-{a+1}_{c}.jpg')
        if stat(f'/home/raylandson/PycharmProjects/atividadesCv/cap-{a+1}_{c}.jpg').st_size < 12000:
            remove(f'/home/raylandson/PycharmProjects/atividadesCv/cap-{a+1}_{c}.jpg')
            break
        c += 1

