#занятие 1
#with open('dd.txt', 'w') as s:
#    s.write('1 2 3 4 5 6')

#w=[]
#d=open('dd.txt', 'r')
#d = d.read().split('\n')
#for i in d:
#    if i !='':
#        if int(i) % 2 == 0:
#            w.append(i)
#p=' '.join(w)
#with open('четные.txt', 'w') as n:
#    n.write(p)

#2
#import string
#import random
#def gen(w):
#    c =  string.digits
#    dd = ''.join(random.choice(c)for _ in range(w))
#    return dd
#s=gen(6)
#p=' '.join(s)
#with open('число.bin', 'wb')as d:
#    d.write(p.encode())

#макс значение
#x = []
#with open('число.bin', 'rb') as s:
#    data = s.read()
#data_str = data.decode()
#numbers = data_str.split()
#l = max(numbers)
#x.append(l)
#l=''.join(x)
#print(l)

#3 простые числа с задания 2
#import math
#with open('число.bin', 'rb') as s:
#    d= s.read().decode()
#def is_prime(number):
#    if number < 2:
#        return False
#    for i in range(2, int(math.sqrt(number)) + 1):
#        if number % i == 0:
#            return False
#    return True
#l=[]
#for number in d:
#    if is_prime(int(number)):
#        l.append(number)
#print(l)

#4 последовательнасть возрастающая или нет
#e = 0
#with open('число.bin', 'rb') as s:
#    g = s.read().decode().split()
#for _ in range(len(g)-1):
#    if (g[e+0])<(g[e+1]):
#        e += 1
#if e==5:
#    print('возрастающая последовательнасть')
#else:
#    print('не возрастающая последовательнасть')

#5 симетричная последовательность
#with open('число.bin', 'rb') as s:
#    g = s.read().decode().split()
#if g==sorted(g)or g[::-1]==sorted(g):
#    print('симетричная последовательность')
#else:
#    print('не симетричная последовательность')

#6 в текстовом обратное число
#with open('dd.txt', 'r') as s:
#    g = s.read().split()
#r=g[::-1]
#with open('обрат.число.txt', 'w') as s:
#    g = s.write(' '.join(r))

#7 в бинарном обратное число
#with open('число.bin', 'rb') as s:
#    g = s.read().decode().split()
#r=g[::-1]
#print('был',g,'стал',r,sep='\n')
#with open('обрат.число.bin', 'wb') as s:
#    g = s.write(' '.join(r).encode()) 

#8 обратная последовательность слов
#with open('слова.txt', 'r',encoding='utf-8') as s:
#    g = s.read().split()
#    e=g[::-1]
#print(e)
#with open('обратная последовательность.txt','w')as s:
#   g=s.write(' '.join(e))

#9 отсортировка чисел
#with open('числа.bin', 'rb') as s:
#    g = s.read().decode().split()
#    d=sorted(g)
#print(d)
#with open('отсорт.числа.bin', 'wb') as s:
#    g = s.write(' '.join(d).encode()) 

#10  насиление стран

#with open('dd.txt', 'w') as s:
#    s.writelines(['Берлин,Германия,3850809,891.3\n',
#                  'Мюнхен,Германия,1576000,310.71\n',
#                  'Париж,Франция,2102650,105.4\n',
#                  'Марсель,Франция,870321,240.62\n'])
# filename = "cities.txt"
# most_populated_city_in_germany = ""
# most_populated_city_in_france = ""
# most_dense_city = ""
# countries_with_large_cities = []
# cities_in_france = 0

# with open('dd.txt', "r") as file:
#     for line in file:
#         city, country, population, area = line.strip().split(",", 3)
#         population = int(population)
#         area = float(area)

#         if country == "Германия":
#             if most_populated_city_in_germany == "" or population > most_populated_city_in_germany[2]:
#                 most_populated_city_in_germany = (city, country, population, area)

#         if country == "Франция":
#             cities_in_france += 1
#             if most_populated_city_in_france == "" or population > most_populated_city_in_france[2]:
#                 most_populated_city_in_france = (city, country, population, area)

#         if most_dense_city == "" or (population / area) > (most_dense_city[2] / most_dense_city[3]):
#             most_dense_city = (city, country, population, area)

#         if population > 1000000 and country not in countries_with_large_cities:
#             countries_with_large_cities.append(country)

# print("Самый населенный город в Германии:", most_populated_city_in_germany[0])
# print("Самый населенный город во Франции:", most_populated_city_in_france[0])
# print("Город с наибольшей плотностью населения:", most_dense_city[0])


#11 определение самой встеречающейся буквы

# with open('dd.txt', 'w') as s:
#     s.writelines('She sells sea shells by the sea shore.')
# with open('dd.txt', "r") as s:
#     d=s.read().lower()
# d=(''.join(d))
# a = {}

# for i in d:
#     if i.isalpha():
#         if i in a:
#             a[i] += 1
#         else:
#             a[i] = 1

# e = max(a.values())
# w = [i for i, count in a.items() if count == e]
# dd = min(w)

# print(f"Самая часто встречающаяся буква: {dd}")

#12 запись студентов
# with open('dd.txt', 'w') as s:
#     s.write('')
# surname = input("Введите фамилию: ")
# name = input("Введите имя: ")
# with open("dd.txt", "r+", encoding='utf-8') as file:
#     # Читаем все строки в файле
#      s = file.read()
#      surname_count = {}
#      for line in s:
#          if surname in line and name in line:
#              print("Студент уже существует в файле.")
#              break
#          if surname in line:
#              surname_count[surname] = surname_count.get(surname, 0) + 1
#      else:
#          personal_code = str(len(s) + 1).zfill(8)
#          if surname in surname_count:
#              personal_code += '2'
#          file.write(f"{len(s)+1}.{surname},{name},перс.код-{personal_code}\n")
#          print(f"Студент добавлен в файл с порядковым номером {len(s)+1} и персональным номером {personal_code}.")

#13 последовательность по алфавиту 
# with open('dd.txt', 'w') as s:
#     s.write('abc123def456.ghi789jkkl0.mno123pqr456.stu789vwx0.yz.')
# with open("dd.txt", "r") as file:
#     s = file.read()
# letter_frequency = {}
# for i in s:
#     if 'a' <= i <= 'z':
#         letter_frequency[i] = letter_frequency.get(i, 0) + 1
# a = sorted(letter_frequency.keys())
# for letter in a:
#     print(f"{letter}: {letter_frequency[letter]}")

