a = [i**2 if i%2!=0 else -1*i**2 for i in range(1, 11)]
b = [i+1 if i<3 else i+j for i in range(1, 25) for j in range(i-1, i)]
c = [i if i%2!=0 else i*3 for i in range(1, 12)]
d = []
print(a)
print(b)
print(c)
