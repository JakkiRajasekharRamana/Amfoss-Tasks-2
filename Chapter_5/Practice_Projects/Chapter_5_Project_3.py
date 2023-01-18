def addToInventory(inventory,addedItems):
    print("Inventory:")
    for i in addedItems:
        if i in inventory:
            inventory[i]=inventory[i]+1
        else:
            inventory.setdefault(i,1)
    return inventory
def displayInventory(inventory):
    total_items = 0
    for k,v in inventory.items():
        print(v,k)
        total_items = total_items + v
    print("Total number of items: " + str(total_items))


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
