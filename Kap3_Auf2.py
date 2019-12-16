# Primzahlen von 1 bis 100 berechnen

for n in range(1,100):
    result = True
    k = 2
    while k < n:
        if n % k == 0: 
            result = False            
        k = k+1
    if result == True and n != 1:
        print(n)
