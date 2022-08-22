'''
Задача 2. "Самая далёка планета"

S = π * a * b (где a и b - длины полуосей элипса)
Чтобы найти наибольшую площадь, достаточно перемножить длины полуосей, так как
π - константа.
'''

def find_farthest_orbit(orbit):
    square = []
    for i in orbit:
        square.append(i[0] * i[1])
    return orbit[square.index(max(square))]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))