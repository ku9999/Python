word = input().strip()+' запретил  букву '
for i in range(ord('а'), ord('я')+1):
    letter = chr(i)
    if letter in word:
        print(word+ f' {letter} ')
    word = word.replace(letter, '')
    if not word:
        break
