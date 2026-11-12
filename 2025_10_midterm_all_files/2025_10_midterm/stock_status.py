def stock_status(number_of_items, days_to_delivery):
    if number_of_items < 0 or (days_to_delivery < 0 and number_of_items == 0):
        return 'Unknown'
    if number_of_items >= 6:
        return 'In stock'
    if number_of_items < 6 and number_of_items >= 1:
        return f'Only {number_of_items} left in stock'
    if number_of_items == 0 and days_to_delivery > 0:
        return f'Available in {days_to_delivery} days'
    if number_of_items == 0 and days_to_delivery == 0:
        return 'Out of stock'
    return 'Unknown'