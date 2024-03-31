row1, col1, row2, col2 =int(input()),int(input()),int(input()),int(input()),
def get_color(row, col):
    if (row + col) % 2 == 0:
        return 1  # 1 - белый цвет
    else:
        return 2  # 2 - черный цвет

# Проверяем, являются ли координаты клеток одного цвета
if get_color(row1, col1) == get_color(row2, col2):
    print("YES")
else:
    print("NO")
