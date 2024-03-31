n=int(input())
d=[25,10,5,1]
c=0
for i in d:
    while n>=i:
        n-=i
        c+=1
print(c)
