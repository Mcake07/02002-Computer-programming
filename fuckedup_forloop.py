streng1 = ''
streng2 = ''
streng3 = ''
streng4 = ''


for i in range(4, -1, -1):
    streng1 += str(i) + ' '

print(streng1)

for k in range(5):
    i = 4 - k * 1
    streng2 += str(i) + ' '

print(streng2)

print('--------------------------------------------------------------------------------------')

for i in range(1, 10, 2):
    streng3 += str(i) + ' '

print(streng3)

for k in range(5):
    i = 1 + (k * 2)
    streng4 += str(i) + ' '

print(streng4)