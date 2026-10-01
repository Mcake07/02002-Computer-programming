from bacterial_growth import bacterial_growth

result = bacterial_growth(100.0, 0.1, 1000.0)
if result != 44:
    print('Test bacterial_growth(100.0, 0.1, 1000.0) returned', result, 'instead of 44')
else:
    print("You got the correct result on the supplied example. Before concluding that your code is correct, you should test more cases.")