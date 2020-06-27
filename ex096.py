from urllib.request import *
import requests

x, y = map(int, input('what is the chapters range?ex 1 4:  ').split())
for a in range(x, y + 1):
    c = 1
    while True:
        url = f'https://unionmangas.top/leitor/mangas/One%20Piece/{a:02}/{c:03}.png'
        page = requests.get(url.replace("\r", "").replace("\n", ""))
        print(f'downloading cap-{a}_{c}')
        print(page.status_code)
        if page.status_code != 200:
            url = f'https://unionmangas.top/leitor/mangas/One%20Piece/{a:02}/{c:03}.jpg'
            page = requests.get(url.replace("\r", "").replace("\n", ""))
            print(page.status_code)
            if page.status_code != 200:
                print('Stopping')
                break
            opener = URLopener()
            opener.addheader('User-Agent', 'whatever')
            filename, headers = opener.retrieve(url, f'cap-{a}_{c}.jpg')
        else:
            opener = URLopener()
            opener.addheader('User-Agent', 'whatever')
            filename, headers = opener.retrieve(url, f'cap-{a}_{c}.png')
        c += 1
