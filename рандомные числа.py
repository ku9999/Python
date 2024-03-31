import random
while True:
    f=random.randint(0,10)
    a=int(input('угодайте число от 0 до 9: '))
    if a==f:
        print('вы угодали')
        break
    else:
        print('к сожелению вы неугодали оно было таким',f)
        
