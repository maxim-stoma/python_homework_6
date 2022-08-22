'''
Задача 5. "Таблицы бинарных арифметических операций"
'''

def print_operation_table(operation, num_rows=9, num_columns=9):
    for row in range(1, num_rows + 1):
        numbers = []
        for column in range(1, num_columns + 1):
            cross = operation(row, column)
            numbers.append(cross)
        print('\t'.join(str(row) for row in numbers))
    print()


print_operation_table(lambda x, y: x + y)
print_operation_table(lambda x, y: x * y)
print_operation_table(lambda x, y: x ** y)
