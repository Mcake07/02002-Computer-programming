def punctuation_ratio(text):
    comma = text.count(', and ')
    nocomma = text.count(' and ') - comma
    if comma == 0 or nocomma == 0:
        return 0.0
    return comma / nocomma