n=10
for i in range (n+1):
    print(i,end='\t')
print() 
# Создаем таблицу, где 1 - если сумма четная, и 0 - если сумма нечетная
for i in range(1, n + 1):
    print(i,end='\t')
    for j in range(1, n + 1):
        summation = i + j
        result = 1 if summation % 2 == 0 else 0
        print(result,end='\t')
    print()

