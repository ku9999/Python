d = 16
for i in range(2, d + 1):
    if all(i % j != 0 for j in range(2, i)):
        print(i)
