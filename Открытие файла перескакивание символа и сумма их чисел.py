with open('dd.txt', 'r') as f:
    total = sum(int(line.strip().replace('$', '')) for line in f)
print('$',total,sep="")
