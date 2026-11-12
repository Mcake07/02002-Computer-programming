def compound_interest(principal, rate, frequency):
    return principal * (1 + rate / frequency) ** frequency - principal