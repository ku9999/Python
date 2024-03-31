import random
rad=['a','A','a','A','a','A']
def dod(fof):
    d=''.join(random.choice(rad)for _ in range(fof))
    return d
n=4
p=dod(n)
print(p)

