
# Funktion zur Ermittlung aller Primzahlen mit Hilfe 
# einer Generator Funktion
def gen_primes():
    counter = 2
    while True:
        divider_found = False
        for i in range(2, counter):
            if counter % i == 0:
                divider_found = True
        if divider_found == False:
            yield counter
        counter = counter + 1

# Die ersten 20 Primzahlen ausgeben
c = 0
for i in gen_primes():
    c = c + 1
    print(i)
    if c > 20:
        break
