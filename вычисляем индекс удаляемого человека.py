a=int(input())
b=int(input())
s=list(range(1,a+1))
e=0
while len(s)>1:
    e=(e+b-1)%len(s)
    s.pop(e)
print(s[0])
