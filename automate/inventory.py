stuff = {'rope': 1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def addToInventory(inv, addedItems):
    for item in addedItems:
        if item not in inv.keys():
            inv[item] = 1
        else:
            inv[item] += 1
    return inv

def displayInventory(inv):
    print("Inventory:")
    item_total = 0
    for k, v in inv.items():
        item_total += inv[k]
        print(str(inv[k]) + ' ' + k)
    print("Total number of items: " + str(item_total))

displayInventory(stuff)
dragonLoot = ['gold coin', 'dagger']
stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)
