'''
Задача 1. "Мимикрия"
'''

transform = lambda x: x # кусок ": Callable[[Any], Any]" добавился самостоятельно при реформате
values = [1, 23, 42, "asdfg"]
transformed_values = list(map(transform, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')