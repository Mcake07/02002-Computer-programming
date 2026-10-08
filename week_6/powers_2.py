import random
n = random.randint(1,25)

numbers = []

for i in range(n):
    numbers.append(2 ** i)

print(numbers)