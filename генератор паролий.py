import string
import random
def gen(length):
    c =  string.digits
    password = ''.join(random.choice(c)for _ in range(length))
    return password
p = int(input("Введите желаемую длину : "))
generated_password = gen(p)
print("Ваш сгенерированный пароль:", generated_password)
