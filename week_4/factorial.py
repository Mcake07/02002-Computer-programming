n = 5
fact_str = ""
solution = 1
for i in range(1, n + 1):
    fact_str = fact_str + str(i)
    solution = solution * i
    print(str(i) + "! =", fact_str, "=", solution)
    fact_str = fact_str + " * "


# Alternativ men knap så god
n = 5
for i in range(1, n + 1):
    fact_str = str(i) + "! = 1"
    solution = 1
    for j in range(2, i +1 ):
        fact_str = fact_str + " * " + str(j)
        solution = solution * j
    print(fact_str + " = " + str(solution))