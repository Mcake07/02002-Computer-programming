import math as m

P0 = 1000
r = 0.15
t = 10

P = P0 * m.exp(r*t)
print(P)

P = 2000
t = 1/r * m.log(P/P0)

months = (t * 12)%12
years = t//1

print(years, months)
print(t)