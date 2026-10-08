def water_height(h0, rain_per_day):
    for i in range(1, len(rain_per_day)):
        h += rain_per_day[i] - 2
        if h < 0:
            h = 0