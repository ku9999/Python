#проверяет сколько если число повторяется то YES если нет NO
a=input()
if a.count(a[0])==len(a):
    print('YES')
else:
    print('NO')
#Проверяет порядок водимых цифр
num = input() 
if num == ''.join(sorted(num)):
    print('YES')
else:
    print('NO')
#Проверяет порядок водимых цифр с право на лево
num=input()
if ''.join(sorted(num,reverse=True))==num:
    print('YES')
else:
    print('NO')
