candies = 103
candies_eaten = 0
wrappers = 0

while candies >= 5:
    candies_eaten = candies_eaten + candies
    wrappers = wrappers + candies
    candies = 0
    if wrappers >= 5:
        candies = candies + wrappers //5
        wrappers = wrappers % 5
    else:
        break
    print(f'Eaten: {candies_eaten}, candies: {candies}, wrappers: {wrappers}')

print(candies_eaten)