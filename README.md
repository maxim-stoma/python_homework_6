# Знакомство с языком Python
## Домашнее задание 5
### Решение пяти задач

1. "Мимикрия".

Написать такое лямбда-выражение 'transformation', чтобы 'transformed_values' получился копией 'values'. Переменная 'transformation' должна быть глобальной, чтобы проверяющая система смогла его найти. Кроме 'transformation' ничего писать не нужно, выводить на экран - тоже.

2. "Самая далёка планета".

Планеты вращаются вокруг звёзд по эллиптическим орбитам. Назовём самой далёкой ту планету, орбита которой имеет самую наибольшую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдёт ту, по которой вращается самая далёкая планета. Круговые орбиты не учитывать (у данной звезды таких нет). При решении использовать списочные выражения. Гарантируется, что такая планета только одна!

3. "Пам-парам парам-пам парам".

Винни Пух попросил посмотреть, есть ли в его стихах ритм. Ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова.ю если во фразе несколько слов, то они разделяются дефисами. Фразу отделяются друг от друга пробелами. Стихотворение вводится с клавиатуры. Если ритм есть, программа должна выводить "Парам пам-пам".

4. "Все равны, как на подбор".

Необходимо написать функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое знакчение некоторой характеристики, и возвращает True, если это так. Для пустого набора объектов, функция так же должна возвращать True. В противном случае, функция должна возвращать False.

5. "Таблицы бинарных арифметических операций".

Необходимо написать код, который выводит таблицу бинарных арифметических операций, таких как сложение, умножение, возведение в степень. Чтобы не копировать один и тот же код и обобщить все три функции до единой функции рисования таблиц, напишите функцию print_operation_table(operation, num_rows=9, num_columns=9), которая принимает в качества аргумента фунцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть выведены на экран.