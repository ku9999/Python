"Задача: Написать функцию, которая принимает число n и возвращает n-е число"
"Фибоначчи."
def fibonacci(n):
    if n in (1,2):
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))
