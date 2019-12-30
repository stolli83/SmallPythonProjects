
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + "  " + k)
        item_total = item_total + v
    print("Total number of items: " + str(item_total))

display_inventory(stuff)

print("\n\n")

def addToInventory(inventory, addedItems):
    d = {}
    for l in addedItems:
        for k, v in inventory.items():
            if l == k:
                inventory[k] = inventory[k] + 1                
            else:
                d.setdefault(l, 1)
            break
    return {**inventory, **d}
    

       
inv = {'gold coin': 42, 'robe': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
display_inventory(inv)


