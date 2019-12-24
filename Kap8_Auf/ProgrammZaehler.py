def zaehlerLesen():
    try:
        with open("counter.txt","r") as counter:
            state = counter.read()
    except FileNotFoundError:
        print("Das counter.txt-File existiert nicht und wird jetzt erstellt")
        with open("counter.txt","w") as counter: 
            counter.write("0")
            return 0
    print("Der aktuelle Zählerwert wurde erfolgreich eingelesen.")
    return int(state)



def zaehlerSchreiben(c):
    with open("counter.txt","w") as counter:        
        c = c + 1        
        counter.write(str(c))
    print("Der Programmzähler-Wert wurde um 1 erhöht und jetzt auf " + str(c) + " gesetzt.")

# Programmausführung
zaehlerSchreiben(zaehlerLesen())

