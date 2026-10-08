import random

def top_k(n,tops):
    sorted = n.sort()
    cut = n[:tops+1]
    return cut

numbers = [random.uniform(1,100) for _ in range(random.randint(11,50))]
k = random.randint(1,10)

print(top_k(numbers, k))