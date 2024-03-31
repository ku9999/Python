#занятие 3

#1
#with open('dd.txt', 'w') as s:
#    s.write('1 2 3 4 5 6 7 8 9')
#e=[]
#a=[]
#with open('dd.txt', 'r') as s:
#    d=s.read().split()
#for i in d:
#    if int(i)%2==0:
#        e.append(i)
#    else:
#        a.append(i)
#with open('четные.txt', 'w') as s:
#    s.write(' '.join(e))
#with open('не четные.txt', 'w') as s:
#    s.write(' '.join(a))


#2
# def input_polynomial():
#     polynomial = []
#     while True:
#         try:
#             coefficient = float(input("Введите коэффициент: "))
#             polynomial.append(coefficient)
#         except ValueError:
#             break
#     return polynomial
# def print_polynomial(polynomial):
#     degree = len(polynomial) - 1
#     for i, coefficient in enumerate(polynomial):
#         if coefficient == 0:
#             continue
#         if i == 0:
#             print(f"{coefficient}", end="")
#         elif i == 1:
#             print(f"{'+' if coefficient > 0 else '-'} {abs(coefficient)}x", end="")
#         else:
#             print(f"{'+' if coefficient > 0 else '-'} {abs(coefficient)}x^{i}", end="")
#     print()
# def evaluate_polynomial(polynomial, x):
#     result = 0
#     for i, coefficient in enumerate(polynomial):
#         result += coefficient * (x ** i)
#     return result
# def add_polynomials(polynomial1, polynomial2):
#     result = []
#     for i in range(max(len(polynomial1), len(polynomial2))):
#         coefficient1 = polynomial1[i] if i < len(polynomial1) else 0
#         coefficient2 = polynomial2[i] if i < len(polynomial2) else 0
#         result.append(coefficient1 + coefficient2)
#     return result
# def multiply_polynomials(polynomial1, polynomial2):
#     result = [0] * (len(polynomial1) + len(polynomial2) - 1)
#     for i, coefficient1 in enumerate(polynomial1):
#         for j, coefficient2 in enumerate(polynomial2):
#             result[i + j] += coefficient1 * coefficient2
#     return result
# def differentiate_polynomial(polynomial):
#     result = []
#     for i in range(1, len(polynomial)):
#         result.append(i * polynomial[i])
#     return result
# def integrate_polynomial(polynomial):
#     result = [0]
#     for i, coefficient in enumerate(polynomial):
#         result.append(coefficient / (i + 1))
#     return result
# # Ввод полинома
# polynomial = input_polynomial()
# # Печать полинома
# print_polynomial(polynomial)
# # Вычисление значения полинома в заданной точке
# x = float(input("Введите значение x: "))
# result = evaluate_polynomial(polynomial, x)
# print(f"Значение полинома в точке {x} равно {result}")
# # Получение суммы двух полиномов
# polynomial1 = input_polynomial()
# polynomial2 = input_polynomial()
# result = add_polynomials(polynomial1, polynomial2)
# print_polynomial(result)
# # Получение произведения двух полиномов
# result = multiply_polynomials(polynomial1, polynomial2)
# print_polynomial(result)
# # Получение производной полинома
# result = differentiate_polynomial(polynomial)
# print_polynomial(result)
# # Получение первообразной полинома
# result = integrate_polynomial(polynomial)
# print_polynomial(result)

#3
# import numpy as np
# from scipy.sparse import coo_matrix
# def input_matrix():
#     """
#     Функция для ввода матрицы.
#     Возвращает список координат и значения ненулевых элементов.
#     """
#     rows = []
#     cols = []
#     data = []
#     while True:
#         try:
#             row, col, value = input("для того чтобы закончит нажмите ENTER Введите строку, столбец и значение (через пробел): ").split()
#             rows.append(int(row))
#             cols.append(int(col))
#             data.append(float(value))
#         except ValueError:
#             break
#     return rows, cols, data
# def print_matrix(rows, cols, data):
#     """
#     Функция для печати матрицы.
#     """
#     matrix = coo_matrix((data, (rows, cols)))
#     print(matrix.toarray())
# def add_matrices(rows1, cols1, data1, rows2, cols2, data2):
#     """
#     Функция для получения суммы двух матриц.
#     """
#     matrix1 = coo_matrix((data1, (rows1, cols1)))
#     matrix2 = coo_matrix((data2, (rows2, cols2)))
#     result = matrix1 + matrix2
#     return result.row, result.col, result.data
# def multiply_matrices(rows1, cols1, data1, rows2, cols2, data2):
#     """
#     Функция для получения произведения двух матриц.
#     """
#     matrix1 = coo_matrix((data1, (rows1, cols1)))
#     matrix2 = coo_matrix((data2, (rows2, cols2)))
#     result = matrix1.dot(matrix2)
#     return result.row, result.col, result.data
# def transpose_matrix(rows, cols, data):
#     """
#     Функция для транспонирования матрицы.
#     """
#     matrix = coo_matrix((data, (cols, rows)))
#     return matrix.row, matrix.col, matrix.data
# # Ввод матрицы
# rows, cols, data = input_matrix()
# # Печать матрицы
# print_matrix(rows, cols, data)
# # Получение суммы двух матриц
# rows1, cols1, data1 = input_matrix()
# rows2, cols2, data2 = input_matrix()
# result_rows, result_cols, result_data = add_matrices(rows1, cols1, data1, rows2, cols2, data2)
# print_matrix(result_rows, result_cols, result_data)
# # Получение произведения двух матриц
# rows1, cols1, data1 = input_matrix()
# rows2, cols2, data2 = input_matrix()
# result_rows, result_cols, result_data = multiply_matrices(rows1, cols1, data1, rows2, cols2, data2)
# print_matrix(result_rows, result_cols, result_data)
# # Транспонирование матрицы
# rows, cols, data = input_matrix()
# result_rows, result_cols, result_data = transpose_matrix(rows, cols, data)
# print_matrix(result_rows, result_cols, result_data)


#4
# import json
# def load_index(filename):
#     """
#     Функция для загрузки предметного указателя из файла.
#     """
#     with open(filename, "r") as f:
#         index = json.load(f)
#     return index
# def save_index(index, filename):
#     """
#     Функция для сохранения предметного указателя в файл.
#     """
#     with open(filename, "w") as f:
#         json.dump(index, f)
# def add_entry(index, word, page):
#     """
#     Функция для добавления элемента в предметный указатель.
#     """
#     if word not in index:
#         index[word] = []
#     index[word].append(page)
# def remove_entry(index, word, page):
#     """
#     Функция для удаления элемента из предметного указателя.
#     """
#     if word in index:
#         index[word].remove(page)
#         if len(index[word]) == 0:
#             del index[word]
# def print_index(index):
#     """
#     Функция для печати предметного указателя.
#     """
#     for word, pages in index.items():
#         print(f"{word}: {', '.join(str(page) for page in pages)}")
# def search_index(index, word):
#     """
#     Функция для поиска номеров страниц для заданного слова.
#     """
#     if word in index:
#         return index[word]
#     else:
#         return []
# def input_index():
#     """
#     Функция для ввода предметного указателя с клавиатуры.
#     """
#     index = {}
#     while True:
#         word = input("Введите слово (или пустую строку для завершения): ")
#         if not word:
#             break
#         pages = input("Введите номера страниц через запятую: ")
#         pages = [int(page.strip()) for page in pages.split(",")]
#         add_entry(index, word, pages)
#     return index
# # Загрузка предметного указателя из файла
# index = load_index("index.json")
# # Добавление элемента в предметный указатель
# add_entry(index, "Python", [1, 3, 5])
# add_entry(index, "Python", [7, 9])
# add_entry(index, "Java", [2, 4, 6])
# add_entry(index, "C++", [8])
# # Удаление элемента из предметного указателя
# remove_entry(index, "Java", 2)
# # Печать предметного указателя
# print_index(index)
# # Поиск номеров страниц для заданного слова
# pages = search_index(index, "Python")
# print(f"Номера страниц для слова 'Python': {pages}")
# # Сохранение предметного указателя в файл
# save_index(index, "index.json")
# # Ввод предметного указателя с клавиатуры
# index = input_index()
# print_index(index)


#5
# import json
# def load_address_book(filename):
#     """
#     Функция для загрузки адресной книжки из файла.
#     """
#     with open(filename, "r") as f:
#         address_book = json.load(f)
#     return address_book
# def save_address_book(address_book, filename):
#     """
#     Функция для сохранения адресной книжки в файл.
#     """
#     with open(filename, "w") as f:
#         json.dump(address_book, f)
# def add_entry(address_book, name, birthday, phone_numbers):
#     """
#     Функция для добавления записи в адресную книжку.
#     """
#     address_book[name] = {"birthday": birthday, "phone_numbers": phone_numbers}
# def remove_entry(address_book, name):
#     """
#     Функция для удаления записи из адресной книжки.
#     """
#     if name in address_book:
#         del address_book[name]
# def print_address_book(address_book):
#     """
#     Функция для печати адресной книжки.
#     """
#     for name, data in address_book.items():
#         print(f"{name}:")
#         print(f"  Birthday: {data['birthday']}")
#         print("  Phone numbers:")
#         for phone_type, phone_number in data["phone_numbers"].items():
#             print(f"    {phone_type}: {phone_number}")
# def search_address_book(address_book, query):
#     """
#     Функция для поиска записей в адресной книжке по заданному признаку.
#     """
#     results = {}
#     for name, data in address_book.items():
#         if query in name:
#             results[name] = data
#         elif query == data["birthday"]:
#             results[name] = data
#         elif query in data["phone_numbers"].values():
#             results[name] = data
#     return results
# def input_address_book():
#     """
#     Функция для ввода адресной книжки с клавиатуры.
#     """
#     address_book = {}
#     while True:
#         name = input("Введите имя (или пустую строку для завершения): ")
#         if not name:
#             break
#         birthday = input("Введите дату рождения: ")
#         phone_numbers = {}
#         while True:
#             phone_type = input("Введите тип телефона (или пустую строку для завершения): ")
#             if not phone_type:
#                 break
#             phone_number = input("Введите номер телефона: ")
#             phone_numbers[phone_type] = phone_number
#         add_entry(address_book, name, birthday, phone_numbers)
#     return address_book
# # Загрузка адресной книжки из файла
# address_book = load_address_book("address_book.json")
# # Добавление записи в адресную книжку
# add_entry(address_book, "John Smith", "01/01/1970", {"home": "123-456-7890", "mobile": "987-654-3210"})
# # Удаление записи из адресной книжки
# remove_entry(address_book, "Jane Doe")
# # Печать адресной книжки
# print_address_book(address_book)
# # Поиск записей в адресной книжке по заданному признаку
# results = search_address_book(address_book, "Smith")
# print_address_book(results)
# # Сохранение адресной книжки в файл
# save_address_book(address_book, "address_book.json")
# # Ввод адресной книжки с клавиатуры
# address_book = input_address_book()
# print_address_book(address_book)


#6
# import json

# # Создание словаря
# catalog ={
#   "To Kill a Mockingbird": {
#     "author": "Harper Lee",
#     "total_copies": 3,
#     "copies_on_hand": 1
#   },
#   "1984": {
#     "author": "George Orwell",
#     "total_copies": 2,
#     "copies_on_hand": 0
#   }
# }

# # Запись словаря в файл
# with open("catalog.json", "w") as f:
#     json.dump(catalog, f)


# def load_catalog(filename):
#     """
#     Функция для загрузки каталога из файла.
#     """
#     with open(filename, "r") as f:
#         catalog = json.load(f)
#     return catalog


# def save_catalog(catalog, filename):
#     """
#     Функция для сохранения каталога в файл.
#     """
#     with open(filename, "w") as f:
#         json.dump(catalog, f)


# def add_book(catalog, title, author, total_copies, copies_on_hand):
#     """
#     Функция для добавления книги в каталог.
#     """
#     catalog[title] = {"author": author, "total_copies": total_copies, "copies_on_hand": copies_on_hand}


# def remove_book(catalog, title):
#     """
#     Функция для удаления книги из каталога.
#     """
#     if title in catalog:
#         del catalog[title]


# def print_catalog(catalog):
#     """
#     Функция для печати каталога.
#     """
#     for title, data in catalog.items():
#         print(f"{title}:")
#         print(f"  Author: {data['author']}")
#         print(f"  Total copies: {data['total_copies']}")
#         print(f"  Copies on hand: {data['copies_on_hand']}")


# def search_catalog(catalog, query):
#     """
#     Функция для поиска книг в каталоге по заданному признаку.
#     """
#     results = {}
#     for title, data in catalog.items():
#         if query in title:
#             results[title] = data
#         elif query == data["author"]:
#             results[title] = data
#     return results


# def input_catalog():
#     """
#     Функция для ввода каталога с клавиатуры.
#     """
#     catalog = {}
#     while True:
#         title = input("Введите название книги (или пустую строку для завершения): ")
#         if not title:
#             break
#         author = input("Введите автора: ")
#         total_copies = int(input("Введите общее количество экземпляров: "))
#         copies_on_hand = int(input("Введите количество экземпляров на руках: "))
#         add_book(catalog, title, author, total_copies, copies_on_hand)
#     return catalog

# # Загрузка каталога из файла
# catalog = load_catalog("catalog.json")

# # Добавление книги в каталог
# add_book(catalog, "The Great Gatsby", "F. Scott Fitzgerald", 5, 2)

# # Удаление книги из каталога
# remove_book(catalog, "To Kill a Mockingbird")

# # Печать каталога
# print_catalog(catalog)

# # Поиск книг в каталоге по заданному признаку
# results = search_catalog(catalog, "Fitzgerald")
# print_catalog(results)

# # Сохранение каталога в файл
# save_catalog(catalog, "catalog.json")

# # Ввод каталога с клавиатуры
# catalog = input_catalog()
# print_catalog(catalog)



#7
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# head = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)

# head.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# from collections import deque
# def print_numbers(head):
#     """
#     Функция для печати чисел из односвязного списка.
#     """
#     stack = []
#     queue = deque()
#     node = head
#     while node is not None:
#         if node.value % 2 == 0:
#             stack.append(node.value)
#         else:
#             queue.append(node.value)
#         node = node.next
#     while len(stack) > 0:
#         print(stack.pop())
#     while len(queue) > 0:
#         print(queue.popleft())


#8
# from collections import deque
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# head = Node(-3)
# node2 = Node(2)
# node3 = Node(0)
# node4 = Node(-5)
# node5 = Node(7)

# head.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# def print_numbers(head):
#     """
#     Функция для печати чисел из односвязного списка.
#     """
#     queue = deque()
#     node = head
#     while node is not None:
#         if node.value < 0:
#             print(node.value)
#         elif node.value > 0:
#             queue.append(node.value)
#         node = node.next
#     while len(queue) > 0:
#         print(queue.popleft())

