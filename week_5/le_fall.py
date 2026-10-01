import math

def falling_time(distance, g = 9.82):
    return math.sqrt((2 * distance) / g)


print(falling_time(24), falling_time(100))