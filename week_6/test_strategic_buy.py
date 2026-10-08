from strategic_buy import strategic_buy

expected = 3
prices = [1, 12, 5, 14, 1000]
output = strategic_buy(prices, 30)
if output != expected:
    print("FAILED the following test:")
print("strategic_buy(", prices, ", 30) returned", output, "should be", expected)

expected = 0
prices = [11, 2, 5, 7, 3]
output = strategic_buy(prices, 1)
if output != expected:
    print("FAILED the following test:")
print("strategic_buy(", prices, ", 1) returned", output, "should be", expected)

expected = 9
prices = [4, 10, 7, 9, 6, 15, 13, 12, 1, 5, 14, 11, 3, 8, 2]
output = strategic_buy(prices, 45)
if output != expected:
    print("FAILED the following test:")
print("strategic_buy(", prices, ", 45) returned", output, "should be", expected)

expected = 0
prices = [] # nothing for sale
output = strategic_buy(prices, 100)
if output != expected:
    print("FAILED the following test:")
print("strategic_buy(", prices, ", 100) returned", output, "should be", expected)