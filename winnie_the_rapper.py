'''
Задача 3. "Пам-парам парам-пам парам"
'''

counting_rhyme = input()
words = counting_rhyme.split()
vowels = ['а', 'о', 'у', 'е', 'ё', 'э', 'и', 'ы', 'ю', 'я']
count = [sum(char in vowels for char in syllable) for syllable in words]
if len(set(count)) != 1:
    print('Пам парам')
else:
    print('Давай по новой, ритма нет...')