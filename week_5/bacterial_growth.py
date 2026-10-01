def bacterial_growth(initial, growth_rate, max_bact):
    amount = initial
    if amount >= max_bact * 0.9:
        return 0
    for t in range(1, 7 * 24 + 1):
        delta_n = growth_rate * amount * (max_bact - amount) / max_bact
        amount += delta_n
        if amount >= max_bact * 0.9:
            return t
    return -1