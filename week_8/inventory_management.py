def restock_inventory(current, add):
    new = {}
    for item in current:
        new[item] = current[item] + add
    return new

inventory = {
    "apples": 10,
    "bananas": 5,
    "oranges": 8,
    "kiwis": 7
}

print(restock_inventory(inventory, 3))