# Ввод двух множеств от пользователя
set1 = set(input("Введите элементы первого множества через пробел: ").split())
set2 = set(input("Введите элементы второго множества через пробел: ").split())

# Объединение двух множеств и сортировка
union_set = sorted(set1.union(set2))

# Вывод объединенного множества
print(' '.join(union_set))
