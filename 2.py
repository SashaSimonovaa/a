a = []
for i in range(1, 11):
    if i%2 == 0: a.append(-(i**2))
    else: a.append(i**2)
print(a)