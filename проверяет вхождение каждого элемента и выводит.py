def count_chars(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

# Тесты
print(count_chars('hello'))
