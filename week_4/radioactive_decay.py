R = 0.9  # remaining fraction after each hour
amount = 2.5

for i in range(1,10):
    amount = amount - amount * 0.1
    print(f'The amount after {i} hours is {amount}')