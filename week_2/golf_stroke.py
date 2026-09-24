import math as m

g = 9.821

v0 = 10
theta = m.radians(45)

R = ((v0 ** 2) * m.sin(2 * theta)) / g
T = (2 * v0 * m.cos(theta)) / g


print(round(R,2), round(T,2))