def number_digits(number):
    if not isinstance(number, int):
        return 'DATATYPE-ERROR - ONLY INTEGER IS ALLOWED'
    if number < 0:
        return 'ERROR - INTEGER CANNOT BE NEGATIVE'

    return len(str(number))
