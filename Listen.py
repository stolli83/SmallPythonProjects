liste=["Apfel","Banane","Birne"]
print(liste)

print(liste[0])

print(liste[-1])

print("Heute ist es sehr kalt".split(" "))

print(" ".join(liste))


einkaufs_korb=["Computer", "Tastatur"]
einkaufs_korb.append("Maus")
print(einkaufs_korb)

print(einkaufs_korb.pop())
print(einkaufs_korb)

einkaufs_korb.extend(["Maus", "Speicherkarte"])
print(einkaufs_korb)

del einkaufs_korb[1]
print(einkaufs_korb)

