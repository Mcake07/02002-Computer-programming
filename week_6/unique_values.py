import random

def unique_values(input_list):
    list = []
    for i in range(len(input_list)):
        before = input_list[:i]
        if not input_list[i] in before:
            list.append(input_list[i])

    return list


x = [random.randint(1,10) for _ in range(random.randint(1,10))]
print(unique_values(x), x)