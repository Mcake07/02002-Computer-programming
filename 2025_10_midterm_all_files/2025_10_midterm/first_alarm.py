def first_alarm(water_levels):
    for i in range(1,len(water_levels) + 1):
        if water_levels[i] > 2:
            return i
        if water_levels[i] - water_levels[i-1] > 0.2 and water_levels[i] == 1.5:
            return i
    return -1

# Wrong