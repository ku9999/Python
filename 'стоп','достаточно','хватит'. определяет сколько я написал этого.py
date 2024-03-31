stop_words=['стоп','достаточно','хватит']
f=0
text=input()
while text.lower() not in stop_words:
    f+=1
    text=input()
print(f)
