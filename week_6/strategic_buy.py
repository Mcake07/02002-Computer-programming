def strategic_buy(prices, budget):
    amount = 0
    prices.sort()
    for i in range(len(prices)):
        if budget >= prices[i]:
            budget -= prices[i]
            amount += 1
    return amount