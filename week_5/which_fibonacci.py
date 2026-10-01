import math

def which_fibonacci(x):
    if x < 1:
        return -1
    golden_ratio = (1 + math.sqrt(5)) / 2
    n = round(math.log(math.sqrt(5) * x, golden_ratio))
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return n if a == x else -1

print(which_fibonacci(14930352))  # 36
print(which_fibonacci(100))       # -1