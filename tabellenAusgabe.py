tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'mouse', 'goose']]

def printTable(table):
    # Ermitteln der maximalen Spaltenbreite
    x=0
    colWiths =[0] * len(tableData)
    for items in tableData:        
        for i in items:
            if len(i) > colWiths[x]:
                colWiths[x] = len(i)
        x=x+1

    x=0
    for items in tableData:
        for i in items:
            print(i.rjust(colWiths[x]))
        print("\n") 
        x=x+1
    
    #TODO: Print result in colums
          

printTable(tableData)
