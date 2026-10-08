import random

def average(numbers):
    return sum(numbers)/len(numbers)

print(average([random.randint(1,100) for _ in range(random.randint(1,25))]))