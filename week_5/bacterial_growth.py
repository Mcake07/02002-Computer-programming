def bacterial_growth(initial, growth_rate, max_bact):
    t = 0
    amount = initial
    while amount < (0.9 * max_bact):
        delta_n = growth_rate * amount * (max_bact - amount) / max_bact
        amount += delta_n
        if t >= 24 * 7:
            return -1
        t += 1
    return t