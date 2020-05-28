words = ('python', 'programming', 'still', 'love', 'market', 'share')
for word in words:
    print(f'\nthe vowels in {word.upper()} are: ', end='')
    for x, a in enumerate(word):
        if a.lower() in 'aeiou':
            print(a, end=' ')
