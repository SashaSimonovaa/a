a = [i**2 if i%2!=0 else -1*i**2 for i in range(1, 11)]
b = [2]
for i in range(1, 11):
    b.append(i+b[i-1])
c = [i if i%2!=0 else i*3 for i in range(1, 12)]
d = [1]
j = 0
for i in range(1, 5):
    d.append(i+d[j])
    d.append(i*d[j+1])
    j += 2
print(a)
print(b)
print(c)
print(d)
