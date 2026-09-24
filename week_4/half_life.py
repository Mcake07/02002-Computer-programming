R = 0.75
amount = 6.5
amount_start = amount
hour = 0

while amount > (amount_start / 2):
    hour += 1
    amount = amount * R
    print(f'The amount after {hour} hours is {amount}')

print(f'Stopped due to the fact that the material has reached its half-life, which is when the amount is at {amount_start / 2} or lower')
