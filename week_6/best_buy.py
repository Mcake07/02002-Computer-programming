import random

def best_buy(prices, budget):
    amount = 0
    left_money = budget
    for i in range(len(prices)):
        if left_money >= prices[i]:
            left_money -= prices[i]
            amount += 1

    return amount


x = [random.randint(1,10) for _ in range(2500)]
y = random.randint(25,1000)

print(best_buy(x,y), y)