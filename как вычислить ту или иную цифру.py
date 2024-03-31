num = input()
#Сумма цифр
sum_digits = sum(int(d) for d in num)
#Количество цифр
count_digits = len(num)
#Произведение цифр
prod_digits = 1
for i in num:
    prod_digits *= int(i)
#Среднее арифметическое цифр
avg_digits = sum_digits / count_digits
#Первая цифра
first_digit = int(num[0])
#Сумма первой и последней цифры
first_last_sum = int(num[0]) + int(num[-1])
#Вывод результатов
print(sum_digits)
print(count_digits)
print(prod_digits)
print(avg_digits)
print(first_digit)
print(first_last_sum)
