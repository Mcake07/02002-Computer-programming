def lucas_number(i):
    if i == 0: return 2
    if i == 1: return 1
    else: return lucas_number(i - 1) + lucas_number (i - 2)