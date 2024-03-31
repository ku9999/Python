import random
s=0
d=0
while s<20 and d<20:
    if input('Нажмите :а: если хотите кинуть монетку =').lower()=='a':
        if random.randint(0,100)<50:
            s+=1
        else:
            d+=1
        print('Орел',d,'Решка',s)
if s==20 and d!=20:
    print('победа Решка')
else:
    print('победа Орел')

    
    
        
