def next_even(number):
    if number % 2 == 0:
        return number + 2
    elif number % -2 == 0:
        return number + 2
    else:
        return number + 1