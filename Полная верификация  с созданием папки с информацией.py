import smtplib
import os

def enter_data():
    # Запросить данные пользователя
    a = input('ИМЯ: ')
    b = int(input('Возраст: '))
    if b < 18:
        print('Вы несовершеннолетний')
    v = input('Профессия: ')
    c = input('Город проживания: ')
    x = input('Gmail: ')
    c=input('коментарии: ')
    info = {'name': a,
            'age': b,
            'job': v,
            'city': c,
            'email': x,
            'kom':c}
    save_data(info)

def save_data(info):
    # Создать папку, если ее нет
    directory = 'данные'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Создать и записать данные в файл
    filename = 'данные/info.txt'
    with open(filename, 'w') as file:
        file.write(f'ИМЯ: {info["name"]}\n')
        file.write(f'Возраст: {info["age"]}\n')
        file.write(f'Профессия: {info["job"]}\n')
        file.write(f'Город проживания: {info["city"]}\n')
        file.write(f'Gmail: {info["email"]}\n')
        file.write(f'коментариии: {info["kom"]}\n')
# Основной код
while True:
    choice = input('Нажмите a, чтобы ввести данные. Нажмите l, чтобы закончить верификацию ')
    if choice.lower() == 'a':
        enter_data()
    elif choice.lower() == 'l':
        send_email()
        break
    else:
        print('Неправильный выбор. Попробуйте снова.')
