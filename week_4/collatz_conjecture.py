n = 99 ** 99
n_start = n
steps = 0

while n != 1:
    if (n % 2) == 0:
        steps += 1
        n = n // 2

    elif (n % 2) > 0:
        steps += 1
        n = 3 * n + 1
    else:
        print('Dude wtf')
        quit()

print(f'The collatz conjecture reached {n} in {steps} steps')