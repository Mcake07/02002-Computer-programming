import math as m

a = 1
b = 1
c = 2

is_triangle = False
triangle_type = "Scalene"

if a<1 or b<1 or c<1:
    print("Invalid")
    quit()

if m.sqrt(a^2 + b^2)!=c^2:
    triangle_type = "Not a triangle"
    print(triangle_type)
    quit()
elif a==b and b==c:
    triangle_type = "Equilateral"
elif (a==b or a==c or b==c) and (a!=b or a!=c or b!=c):
    triangle_type = "Isosceles"
elif a!=b and a!=c and b!=c:
    triangle_type = "Scalene"

print(triangle_type)