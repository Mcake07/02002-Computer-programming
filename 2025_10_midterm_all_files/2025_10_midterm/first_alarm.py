def first_alarm(water_levels):
    for i in range(len(water_levels)):
        if water_levels[i] > 2.0: return i
        elif i > 0:
            if water_levels[i] - water_levels[i-1] > 0.2 and water_levels[i] > 1.5:
                return i
    return -1