a = [i**2 if i%2!=0 else -1*i**2 for i in range(1, 11)]
b = [2]
for i in range(1, 11):
    b.append(i+b[i-1])
c = [i if i%2!=0 else i*3 for i in range(1, 12)]
d = [1]
for i in range(1, 4):
    d.append(i+d[i-1])
    d.append(d[i-1]*d[i])
print(a)
print(b)
print(c)
print(d)
