liste = [3, 5, 13, 22, 37, 42, 54, 68, 71 ]
liste2 = []

for i in liste:
    if i != 42:
        i = i * 10
        liste2.append(i)
print(liste2)


liste3 =[i * 10 for i in liste if i != 42]
print(liste3)