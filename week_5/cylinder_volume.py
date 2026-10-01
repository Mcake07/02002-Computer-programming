import math as m

def disc_area(r):
    return m.pi * r ** 2

def cylinder_volume(r,h):
    return disc_area(r) * h