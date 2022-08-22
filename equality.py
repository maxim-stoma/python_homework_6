'''
Задача 4. "Все равны, как на подбор".
'''

def same_by(characteristic, objects):
    return all(not characteristic(i) for i in objects)


values = [1, 2, 5, 10]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')