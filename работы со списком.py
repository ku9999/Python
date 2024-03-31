#a = int(input())
#l=[]
#for i in range(a):
#    a=chr(ord('a')+i)
#    l.append(a)
#print(alphabet)
#
#n = int(input())
#outer_list = []
#for i in range(1, n+1):
#    inner_list = []
#    for j in range(1, i+1):
#        inner_list.append(j)
#    outer_list.append(inner_list)
#    print(inner_list)



#s=input().split()
#result=[]
#for i in s:
#    result.append([i])
#print(result)
string = input().split()  # считываем строку и разбиваем на список символов

result = []
current = []  # текущий подсписок

for s in string:
    if not current or current[0] == s:  # если текущий подсписок пуст или первый символ равен текущему символу
        current.append(s)  # добавляем текущий символ
    else:  # если первый символ не равен текущему символу
        result.append(current)  # добавляем текущий подсписок в результат
        current = [s]  # создаем новый подсписок с текущим символом

result.append(current)  # добавляем последний подсписок в результат

print(result)

#lst = input().split()
#result = [[]]
#for length in range(1, len(lst)+1):
#    for start in range(len(lst)-length+1):
#        sublist = lst[start:start+length]
#        result.append(sublist)
#print(result)
