a=int(input())
f=""
while a>0:
    f=str(a%2)+f
    a//=2
print(f)
